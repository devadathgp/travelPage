from rest_framework import serializers
from . models import *

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model=TravelPage
        fields='__all__'