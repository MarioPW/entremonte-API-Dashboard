from django.contrib import admin
from .models import Slider

@admin.register(Slider)
class Slider_Admin(admin.ModelAdmin):
    list_display = ('title', 'url')
    list_display_links = ('title',)
    search_fields = ('title',)
