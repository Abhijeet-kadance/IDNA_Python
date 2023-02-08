from rest_framework import serializers

from .models import TestData

class TestSerializer(serializers.HyperlinkModelSerializer):
    class Meta:
        model = TestData
        fields = ('name','description')