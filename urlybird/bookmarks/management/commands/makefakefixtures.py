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
                    'user': choice(User.objects.all()),
                    'flink': fake.image_url(),
                    'slink': fake.password(length=6, special_chars=False),
                    'timestamp': fake.date_time_this_year(),
                    'wtitle': fake.lorem(max_nb_chars=100),
                    'winfo': fake.lorem(max_nb_chars=255),
                },
            }
            worm_data.append(worm)

        with open('bookmarks/fixtures/worms.json', 'w') as f:
            f.write(json.dumps(worm_data))


#
