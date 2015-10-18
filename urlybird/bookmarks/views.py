from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.timezone import make_aware
from urlybird.forms import UserForm, WormForm
from django.views import generic
from .models import Worm, Click
from faker import Faker
from django.contrib.auth.decorators import login_required


# Create your views here.

class WormListView(generic.ListView):
    template_name = 'bookmarks/recent_worms.html'
    context_object_name = 'worms'
    paginate_by = 25

    def get_queryset(self):
        self.form = WormForm()
        return Worm.objects.all().order_by('-timestamp') \
            .prefetch_related('user')


class BirdListView(generic.ListView):
    template_name = 'bookmarks/bird_list.html'
    context_object_name = 'worms'
    paginate_by = 25

    def get_queryset(self):
        self.form = WormForm()
        self.user = get_object_or_404(User, pk=self.kwargs['pk'])
        return self.user.worm_set.all().order_by('-timestamp') \
            .prefetch_related('user').prefetch_related('click')


class ClickListView(generic.ListView):
    model = Click
    template = 'bookmarks/click_list.html'
    context_object_name = 'clicks'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(ClickListView, self).get_context_data(**kwargs)
        context['worm'] = Worm.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Click.objects.filter(worm=Worm.objects.get(
            pk=self.kwargs['pk'])).order_by('-timestamp') \
            .prefetch_related('worm', 'user')


def add_worm(request):
    if request.method == 'POST':
        form = WormForm(request.POST)
        if form.is_valid():
            worm = form.save(commit=False)
            if request.user.is_authenticated():
                worm.user = request.user
            fake = Faker()
            while True:
                slink = fake.password(length=7, special_chars=False)
                if len(Worm.objects.filter(slink=slink)) == 0:
                    worm.slink = slink
                    break
                continue
            worm.timestamp = make_aware(datetime.now())
            worm.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'You successfully got that worm!')
        else:
            messages.add_message(request,
                                 messages.ERROR,
                                 'Form data invalid, all fields required')
    else:
        messages.add_message(request,
                             messages.ERROR,
                             'Stop trying to hack this site!')
    return redirect(request.GET['next'])


def redirect_slink(request, slink):
    worm = get_object_or_404(Worm, slink=slink)
    click = Click(worm=worm, timestamp=make_aware(datetime.now()))
    if request.user.is_authenticated():
        click.user = request.user
    click.save()
    return redirect(worm.flink.strip())


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect(reverse('bird_list', args=[user.pk]))
        else:
            messages.add_message(request, messages.ERROR, 'ERROR LOGGING IN!')
            return render(request,
                          'bookmarks/user_login.html',
                          {'username': username})
    else:
        return render(request, 'bookmarks/user_login.html')


def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            password = form['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=user.username, password=password)
            login(request, user)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Your account was successfully created.')
            return redirect('user_login')
    else:
        form = UserForm()
    return render(request,
                  'bookmarks/user_register.html',
                  {'form': form})


def user_logout(request):
    if request.user.is_authenticated():
        user_name = request.user.username
        logout(request)
        messages.add_message(request, messages.SUCCESS,
                             "{}, you have successfully logged out".format(
                                 user_name))
        return redirect('/')


@login_required
def delete_worm(request, worm_id):
    if Worm.objects.get(pk=worm_id).user == request.user:
        Worm.objects.get(pk=worm_id).delete()
        messages.add_message(request, messages.SUCCESS, "Worm removed")
        return redirect('bird_list', pk=request.user.pk)
    else:
        messages.add_message(
            request, messages.ERROR, "You do not have access")
        return redirect('recent_worms')


@login_required
def edit_worm(request, worm_id):
    worm = get_object_or_404(Worm, pk=worm_id)
    flink = worm.flink
    wtitle = worm.wtitle
    winfo = worm.winfo
    if request.method == 'GET':
        form = WormForm(instance=worm)
    elif request.method == 'POST':
        form = WormForm(instance=worm, data=request.POST)
        if form.is_valid():
            worm = form.save(commit=False)
            worm.flink = flink
            worm.wtitle = wtitle
            worm.winfo = winfo
            worm.timestamp = datetime.now()
            worm.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Updated worm')
    return render(request,
                  'bookmarks/edit_worm.html',
                  {'flink': flink,
                   'wtitle': wtitle,
                   'form': form})
