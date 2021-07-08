from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_auth.models import TokenModel

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from .serializers import UsersLoginSerializer, UsersRegisterSerializer, ModeratorsLoginSerializer, ModeratorsRegisterSerializer


class UsersRegisterView(CreateAPIView):
    serializer_class = UsersRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response('Success', status=status.HTTP_201_CREATED)


class UsersLoginView(GenericAPIView):
    serializer_class = UsersLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            token = TokenModel.objects.get(user=user)
            return Response({'key': token.key}, status=status.HTTP_201_CREATED)
        return Response('Invalid login', status=status.HTTP_401_UNAUTHORIZED)


class ModeratorsRegisterView(UsersRegisterView):
    serializer_class = ModeratorsRegisterSerializer


class ModeratorsLoginView(UsersLoginView):
    serializer_class = ModeratorsLoginSerializer
