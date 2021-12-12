from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Users
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json

class UserListAPI(APIView):

    # GET: 전체 user list
    def get(self, request):

        users = Users.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)
    
    # POST
    def post(self, request):

        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):

    # GET
    def get(self, request, uid):

        user = get_object_or_404(Users, uid = uid)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # PUT
    def put(self, request, uid):

        user = get_object_or_404(Users, uid = uid)
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DEL
    def delete(self, request, uid):

        user = get_object_or_404(Users, uid = uid)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        