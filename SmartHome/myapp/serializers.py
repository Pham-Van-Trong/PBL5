from rest_framework import serializers
from .models import Item, ArduinoData


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ArduinoDataSerialezer(serializers.ModelSerializer):
    class Meta:
        model = ArduinoData
        fields = '__all__'

