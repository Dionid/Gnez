from rest_framework import serializers
from .models import BaseForm, SeekerForm, OwnerForm


# class BaseFormSerializer(serializers.ModelSerializer)):


class SeekerFormSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = SeekerForm
        fields = ('id', 'text', 'author')


class OwnerFormSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = OwnerForm
        fields = ('id', 'text', 'author')
