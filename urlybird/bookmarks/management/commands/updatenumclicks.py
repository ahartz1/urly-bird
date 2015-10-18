from django.core.management.base import BaseCommand
from bookmarks.models import Worm


class Command(BaseCommand):

    def handle(self, *args, **options):
        worms = Worm.objects.all()
        for worm in worms:
            worm.numclicks = worm.click_set.all().count()
            worm.save()
