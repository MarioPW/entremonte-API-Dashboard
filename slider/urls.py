from django.urls import path, include
from rest_framework import routers
from slider.views import Slider_view

router = routers.DefaultRouter()
router.register(r'slider',Slider_view,'slider')
urlpatterns = [
    path("", include(router.urls))
]