from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json

class UserListAPI(APIView):

    # POST
    '''
    uid 받아서 있는지 찾아보고 없으면 추가
    '''
    def post(self, reques, uid):

        user = User.objects.filter(uid = uid)
        
        if user.count() is not 0:
            return HttpResponse('BAD REQUEST', status = 400)
    
        ret = User(
            uid = uid
        )
        ret.save()

        return HttpResponse(json.dumps(list(ret)), status = 200)
    # GET
    '''
    uid 받아서 있는지 찾아보고 있으면 Response
    '''
    def get(self, request, uid):

        user = User.objects.filter(uid = uid)
        
        if user.count() is 0:
            return HttpResponse('BAD REQUEST', status = 400)

        return HttpResponse(json.dumps(list(user)), status = 200)

    # PUT
    '''
    uid 받아서 있는지 찾아보고 있으면 수정
    '''
    def put(self, request, uid):
        return HttpResponse('BAD REQUEST', status = 400)

    '''
    uid 받아서 있는지 찾아복 있으면 삭제
    '''
    # DEL
    def delete(self, request, uid):
        return HttpResponse('BAD REQUEST', status = 400)

        