from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from urlybird.forms import UserForm
from django.views import generic
from .models import Worm


# Create your views here.

class WormListView(generic.ListView):
    template_name = 'bookmarks/recent_worms.html'
    context_object_name = 'worms'
    paginate_by = 25

    def get_queryset(self):
        return Worm.objects.all().order_by('-timestamp')


class BirdListView(generic.ListView):
    template_name = 'bookmarks/bird_detail.html'
    context_object_name = 'birds'
    paginate_by = 25

    def get_queryset(self):
        return self.user.worm_set.all().order_by('-timestamp')


class WormDetailView(generic.DetailView):
    model = Worm
    template = 'bookmarks/worm_detail.html'


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect(reverse('bird_detail', args=[user.pk]))
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
                             "You have successfully logged out")
        return render(request,
                      'bookmarks/user_logout.html',
                      {'user_name': user_name})
    else:
        return redirect('/')
