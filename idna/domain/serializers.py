from rest_framework import serializers

from .models import TestData

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestData
        fields = ('name','description')