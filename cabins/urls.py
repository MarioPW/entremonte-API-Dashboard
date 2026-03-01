from django.urls import path, include
from rest_framework import routers
from cabins.views import Cabin_view, Review_view, Cabin_image_view

router = routers.DefaultRouter()
router.register(r'cabins',Cabin_view,'cabins')
urlpatterns = [
    path("", include(router.urls)),
    path('review/', Review_view.as_view(), name='cabin-review'),
    path('gallery/', Cabin_image_view.as_view(), name='cabin-images'),
]