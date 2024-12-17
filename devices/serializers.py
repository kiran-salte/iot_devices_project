from rest_framework import serializers
from .models import Payload, Device
import base64

#Serailizer for paylaod model
class PayloadSerializer(serializers.ModelSerializer):
    rx_info = serializers.JSONField(default=dict)
    tx_info = serializers.JSONField(default=dict)

    class Meta:
        model = Payload
        fields = '__all__'


#Serailizer for Device model
class DeviceSerializer(serializers.ModelSerializer):
    payloads = PayloadSerializer(many=True)

    class Meta:
        model = Device
        fields = ['devEUI', 'payloads']
