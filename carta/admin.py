from django.contrib import admin
from .models import Item, Category

@admin.register(Category)
class Categories_Admin(admin.ModelAdmin):
    list_display_links = ('category',)
    list_display = ('category','available', 'possition')
    list_editable = ('available', 'possition')
    search_fields = ('category',)

# Panel Configuration
@admin.register(Item)
class Items_Admin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ('name', 'category', 'available','price')
    list_editable = ('available','category','price')
    search_fields = ('name', 'category')

admin.site.site_header = 'Entremonte Admin'
admin.site.site_title = 'Entremonte Admin'
admin.site.index_title = 'Admin Panel'
