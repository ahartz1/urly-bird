from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import json
from random import choice
from faker import Faker


class Command(BaseCommand):

    def handle(self, *args, **options):
        # 1. Make some fake users
        fake = Faker()

        for _ in range(6000):
            while True:
                fake_username = fake.user_name() + choice(list('0123456789'))
                try:
                    user = User.objects.create_user(fake_username,
                                                    fake.email(),
                                                    'password')
                    user.save()
                    break
                except:
                    continue


        # 2. Make some fake worms, then create a json from them
        worm_data = []

        for _ in range(100000):
            worm = {
                'model': 'bookmarks.Worm',
                'fields': {
                    'flink': fake.,
                    'gender': row['Gender'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
            }
            worm_data.append(user)

        with open('bookmarks/fixtures/worms.json', 'w') as f:
            f.write(json.dumps(worm_data))


















#
