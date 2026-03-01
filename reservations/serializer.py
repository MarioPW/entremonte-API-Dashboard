from rest_framework import serializers
from .models import Reservation, Reservation_request

class ReservationSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    cabin_name = serializers.CharField(source='cabin.name', read_only=True)
    date_date = serializers.DateField(source='date.date', read_only=True)

    class Meta:
        model = Reservation
        fields = [
            'id',
            'user_email',
            'cabin_name',
            'date_date',
            'dishes_order1',
            'dishes_order2',
        ]
        read_only_fields = ['id', 'user_email', 'cabin_name', 'date_date']

class Reservation_requestSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Reservation_request
        fields = [
            'checkin',
            'checkout',
            'user_phone',
            'date',
            'user_email'
        ]
        read_only_fields = ['date']