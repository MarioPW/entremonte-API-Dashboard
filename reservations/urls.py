from django.urls import path, include
from rest_framework import routers
from reservations.views import Reservation_request_view

router = routers.DefaultRouter()
router.register(r'reservations', Reservation_request_view, 'reservations')

urlpatterns = [
    path("", include(router.urls)),
]
