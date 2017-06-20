from rest_framework import generics
from .models import BaseForm
from .serializers import BaseFormSerializer
from rest_framework import permissions


class BaseFormList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = BaseForm.objects.all()
    serializer_class = BaseFormSerializer
