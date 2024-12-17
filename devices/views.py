from django.shortcuts import render
import base64
from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views.generic import ListView
from .models import Device, Payload
from .serializers import PayloadSerializer, DeviceSerializer

def base64_to_hex(data):
    decoded_data = base64.b64decode(data)
    return decoded_data.hex()

class DeviceViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permissions_class = [IsAuthenticated]
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    @action(detail=True, methods=['get'])
    def payloads(self, request, pk=None):
        device = self.get_object()
        payloads = device.payloads.all()
        serializer_class = PayloadSerializer(payload, many=True)
        return Response(serializer.data)


class PayloadViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PayloadSerializer

    def create(self, request):
        if not request.data.get('devEUI') or not request.data.get('fCnt') or not request.data.get('data'):
            return Response({'error': 'Invalid payload data'}, status=status.HTTP_400_BAD_REQUEST)

        # Extract the payload data
        data = request.data
        devEUI = data.get('devEUI')
        fCnt = data.get('fCnt')
        payload_data = data.get('data')
        rx_info = data.get('rxInfo')
        tx_info = data.get('txInfo')

        # Get or create the Device instance
        device, created = Device.objects.get_or_create(devEUI=devEUI)

        # Check for duplicate payload for the same device and fCnt
        if Payload.objects.filter(devEUI=device, fCnt=fCnt).exists():
            return Response({'error': 'Duplicate message'}, status=status.HTTP_400_BAD_REQUEST)

        hex_value = base64_to_hex(payload_data)
        payload_status = 'passing' if hex_value == '01' else 'failing'

        # Create the Payload instance
        payload = Payload.objects.create(
            devEUI=device,
            fCnt=fCnt,
            data=payload_data,
            rx_info=rx_info,
            tx_info=tx_info,
            status=payload_status
        )

        # Update the device's latest status based on the payload's status
        device.save()

        # Return the serialized payload data as a response
        return Response(PayloadSerializer(payload).data, status=status.HTTP_201_CREATED)

#Device ListView to display all devices details
class DeviceListView(ListView):
    model = Device
    template_name = 'device_list.html'
    context_object_name = 'devices'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['devices'] = DeviceSerializer(self.get_queryset(), many=True).data
        return context
