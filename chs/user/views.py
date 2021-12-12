from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class UserListAPI(APIView):

    # POST
    '''
    uid 받아서 있는지 찾아보고 없으면 추가
    '''
    def post(self, reques, uid):

        
        return HttpResponse('BAD REQUEST', status = status.HTTP_400_BAD_REQUEST)
    
    # GET
    '''
    uid 받아서 있는지 찾아보고 있으면 Response
    '''
    def get(self, request, uid):

        if uid == None:
            return HttpResponse('BAD REQUEST', status = status.HTTP_400_BAD_REQUEST)
        return HttpResponse('BAD REQUEST', status = status.HTTP_400_BAD_REQUEST)

    # PUT
    '''
    uid 받아서 있는지 찾아보고 있으면 수정
    '''
    def put(self, request):
        return HttpResponse('BAD REQUEST', status = status.HTTP_400_BAD_REQUEST)

    '''
    uid 받아서 있는지 찾아복 있으면 삭제
    '''
    # DEL
    def delete(self, request):
        return HttpResponse('BAD REQUEST', status = status.HTTP_400_BAD_REQUEST)

        