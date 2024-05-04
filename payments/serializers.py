from rest_framework import serializers

from .models import Payment, Gateway

class GatewaySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = ('id', 'title', 'description', 'avatar')