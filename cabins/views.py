from rest_framework import viewsets, generics
from .serializer import Cabin_serializer, Review_serializer,Cabin_image_serializer
from .models import Cabin, Cabin_review, Cabin_image

class Cabin_view(viewsets.ModelViewSet):
    serializer_class = Cabin_serializer
    queryset = Cabin.objects.all()
    http_method_names = ["get"]

class Review_view(generics.ListCreateAPIView):
    serializer_class = Review_serializer
    http_method_names = ["get","post"]
    def get_queryset(self):
        return Cabin_review.objects.filter(show=True)
    
class Cabin_image_view(generics.ListAPIView):
    serializer_class = Cabin_image_serializer
    queryset = Cabin_image.objects.all()
    http_method_names = ["get"]