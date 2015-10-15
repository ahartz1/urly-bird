from django.contrib import admin
from .models import Worm, Click

class WormAdmin(admin.ModelAdmin):
    list_display = ['flink', 'slink', 'user', 'timestamp', 'wtitle', 'winfo', 'numclicks']


class ClickAdmin(admin.ModelAdmin):
    list_display = ['user', 'worm', 'timestamps']

# Register your models here.

admin.site.register(Worm, WormAdmin)
admin.site.register(Click, ClickAdmin)
