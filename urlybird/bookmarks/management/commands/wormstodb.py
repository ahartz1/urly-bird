from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from random import choice
from faker import Faker
from bookmarks.models import Worm


class Command(BaseCommand):

    def handle(self, *args, **options):
        fake = Faker()
        # 2. Make some fake worms
        for _ in range(6000):
            while True:
                slink = fake.password(length=7, special_chars=False)
                if len(Worm.objects.filter(slink=slink)) == 0:
                    worm = Worm(
                        user=choice(User.objects.all()),
                        flink=fake.image_url(),
                        slink=slink,
                        timestamp=make_aware(fake.date_time_this_year()),
                        wtitle=fake.text(max_nb_chars=100),
                        winfo=fake.text(max_nb_chars=255))
                    worm.save()
                    break
                continue
