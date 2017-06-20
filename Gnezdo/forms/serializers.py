from rest_framework import serializers
from .models import BaseForm


class BaseFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseForm
        fields = ('id', 'text')
