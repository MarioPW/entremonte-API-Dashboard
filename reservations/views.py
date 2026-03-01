from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializer import Reservation_requestSerializer

class Reservation_request_view(viewsets.ModelViewSet):
    serializer_class = Reservation_requestSerializer
    http_method_names = ["post"]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)