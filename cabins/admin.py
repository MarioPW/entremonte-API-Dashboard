from django.contrib import admin
from .models import Cabin, Cabin_service, Cabin_image, Cabin_review

@admin.register(Cabin)
class CabinAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "available",
        "price",
        "capacity",
        "get_services",
        "get_images",
    )
    list_display_links = ("name",)
    list_editable = (
        "available",
        "price",
        "capacity",
    )
    search_fields = ("name", "services__name")
    list_filter = ("available", "services")

    def get_services(self, obj):
        return ", ".join(obj.services.values_list("name", flat=True))

    def get_images(self, obj):
        return ", ".join(obj.images.values_list("image", flat=True))
    
    get_services.short_description = "Servicios"
    get_images.short_description = "Imágenes"


@admin.register(Cabin_service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Cabin_image)
class CabinImageAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Cabin_review)
class CabinReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "rating", "comment", "creation_date", "show")
    list_editable = ("show",)
    search_fields = ("user__username", "comment")
    list_filter = ("rating",)
    ordering = ("-creation_date",)
