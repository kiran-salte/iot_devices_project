from django.db import models

#Constants for the status
PASSING = 'passing'
FAILING = 'failing'
PENDING = 'pending'

STATUS_CHOICES = [
    (PASSING, 'Passing'),
    (FAILING, 'Failing'),
    (PENDING, 'pending')
]

#Device Model
class Device(models.Model):
    devEUI = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.devEUI

#Payload Model 
class Payload(models.Model):
    devEUI = models.ForeignKey(Device, related_name='payloads', on_delete=models.CASCADE)
    fCnt = models.IntegerField()
    data = models.CharField(max_length=256)
    rx_info = models.JSONField(default=dict)
    tx_info = models.JSONField(default=dict)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    class Meta:
        unique_together = ('devEUI', 'fCnt')

    def __str__(self):
        return f"Payload {self.fCnt} for {self.devEUI}"
