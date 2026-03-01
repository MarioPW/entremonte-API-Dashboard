from rest_framework import viewsets
from .serializer import Slider_serializer
from .models import Slider


class Slider_view(viewsets.ModelViewSet):
    serializer_class = Slider_serializer
    queryset = Slider.objects.all()
    http_method_names = ["get"]