from rest_framework import generics
from .models import SeekerForm, OwnerForm
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model
from .serializers import SeekerFormSerializer, OwnerFormSerializer
from rest_framework import permissions
import pdb

class SeekerFormList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = SeekerForm.objects.all()
    serializer_class = SeekerFormSerializer

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

    # def post(self, request, format=None):
    #     form = SeekerFormSerializer(data=request.data)
    #     form.author = request.user
    #     if form.is_valid():
    #         form.save()
    #         pdb.set_trace()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SeekerFormDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = SeekerForm.objects.all()
    serializer_class = SeekerFormSerializer


class OwnerFormList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = OwnerForm.objects.all()
    serializer_class = OwnerFormSerializer
