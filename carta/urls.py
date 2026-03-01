from django.urls import path, include
from rest_framework import routers
from carta.views import Item_view, Category_view

router = routers.DefaultRouter()
router.register(r'items',Item_view,'items')
router.register(r'categorias',Category_view,'categorias')
urlpatterns = [
    path("carta/", include(router.urls))
]
