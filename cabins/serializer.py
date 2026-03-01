from rest_framework import serializers
from .models import Cabin, Cabin_review, Cabin_image

class Cabin_serializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()

    class Meta:
        model = Cabin
        fields = [
            'id',
            'available',
            'price',
            'name',
            'description',
            'capacity',
            'images',
            'services',
            'reviews',
        ]

    def get_images(self, obj):
        def optimize_url(url):
            return url.replace("/upload/", "/upload/f_auto,q_auto/")
        
        return [optimize_url(img.image.url) for img in obj.images.all() if img.image]

    def get_services(self, obj):
        return [service.name for service in obj.services.all()]
    
    def get_reviews(self, obj):
        return [review.comment for review in obj.reviews.all()]

class Review_serializer(serializers.ModelSerializer):
    class Meta:
        model = Cabin_review
        fields = [
            'rating',
            'comment',
            'user',
        ]

class Cabin_image_serializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Cabin_image
        fields = ['id', 'name', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url if obj.image else None
        optimized_url = self.optimize_url(image_url)

        # Devuelve URL completa
        if request:
            return request.build_absolute_uri(optimized_url)
        return optimized_url

    def optimize_url(self, url):
        return url.replace("/upload/", "/upload/f_auto,q_auto/") if url else None