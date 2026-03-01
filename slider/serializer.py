from rest_framework import serializers
from .models import Slider

class Slider_serializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Slider
        exclude = ["id"]

    def get_url(self, obj):
        if not obj.url:
            return None
        return self.optimize_url(obj.url.url)

    def optimize_url(self, url):
        return url.replace("/upload/", "/upload/f_auto,q_auto/")