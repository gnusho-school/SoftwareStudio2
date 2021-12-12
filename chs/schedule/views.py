from django.shortcuts import render
from django.http import HttpResponse
from .models import Work, ShortTerm, LongTerm
from user.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class WorkListAPI(APIView):
    
    # POST
    def post(self, request, **kwargs):

        uid = kwargs.get('uid', None)
        user = User.objects.get(uid = uid)

        work_type = request.GET.get('type', None)
        title = request.GET.get('title', None)
        date = request.GET.get('date', None)

        # 하루에 끝나는 일
        if work_type == 'short term':
            
            start_time = request.GET.get('start_time', None)
            end_time = request.GET.get('end_time', None)

            ret = ShortTerm(
                    title = title,
                    uid = user,
                    date = date,
                    start_time = start_time,
                    end_time = end_time,
                    status = 'O'
                )
            ret.save()
            return HttpResponse(ret, status = status.HTTP_200_OK)
        
        # 장기간 계속 이어지는 일
        elif work_type == 'long term':

            end_date = request.GET.get('end_date')

            ret = LongTerm(
                    title = title,
                    uid = user,
                    date = date,
                    end_date = end_date,
                    status = 'O'
                )
            ret.save()
            return HttpResponse(ret, status = status.HTTP_200_OK)
        
        # 며칠에 한번씩 반복되는 일
        # 날짜 계산을 해준 뒤, 집어넣어줘야함
        elif work_type == 'repeat':
            return HttpResponse(work_type, status = status.HTTP_200_OK)

        return HttpResponse('BAD REQUEST', status = status.HTTP_400_BAD_REQUEST)
    
    # GET
    '''
    두가지 종류
    1. 기간을 주면 그 기간 안에 있는 일들 Response
    2. 하루를 주면 그 날에 있는 일들 Response
    '''
    def get(self, request, **kwargs):

        uid = kwargs.get('uid')

        start_date = request.GET.get('start_date')

        return HttpResponse('GET', status = status.HTTP_200_OK)

    # PUT
    '''
    GET 이후에 실행되므로 pk와 관련 정보를 바로 받아서 수정 
    '''
    def put(self, request, **kwargs):

        uid = kwargs.get('uid')
        return HttpResponse('PUT', status = status.HTTP_200_OK)

    '''
    GET 이후에 실행되므로 pk를 바로 받아서 삭제
    '''
    # DEL
    def delete(self, request, **kwargs):

        uid = kwargs.get('uid')
        return HttpResponse('DEL', status = status.HTTP_200_OK)