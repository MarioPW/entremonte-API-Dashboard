from django.contrib import admin
from .models import Slider

@admin.register(Slider)
class Slider_Admin(admin.ModelAdmin):
    def short_id(self, obj):
        return str(obj.id)[:5] + '...'
    short_id.short_description = 'ID (abreviado)'
    
    list_display = ('short_id', 'title', 'url', 'message')
    list_display_links = ('short_id', 'title','message',)
    search_fields = ('title',)