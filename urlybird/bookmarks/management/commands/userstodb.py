from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from random import choice
from faker import Faker


class Command(BaseCommand):

    def handle(self, *args, **options):
        # 1. Make some fake users
        fake = Faker()

        for _ in range(800):
            while True:
                fake_username = fake.user_name() + \
                    choice(list('0123456789'))
                try:
                    user = User.objects.create_user(fake_username,
                                                    fake.email(),
                                                    'password')
                    user.save()
                    break
                except:
                    continue
