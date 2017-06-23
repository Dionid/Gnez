from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework import permissions
from rest_framework.response import Response
import pdb


class VkView(APIView):
    def get(request, *args, **kwargs):
        return Response({'hello': 'vk'})

    def post():
        print(args)


User = get_user_model()

class UsersList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
