from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Work, ShortTerm, LongTerm
from .serializer import ShortTermSerializer, LongTermSerializer
from user.models import Users
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime
import json

# title = request.GET.get('title', None) -> query parameter 사용

class WorkListAPI(APIView):
    # GET
    def get(self, request):
        
        user = request.GET.get('user', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        
        if start_date is None or end_date is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        # ShortTerm work queryset
        shortTerm = ShortTerm.objects.filter(
            Q(user = user) & Q(date__range = [start_date, end_date])
        )
        
        shortTermSerializer = ShortTermSerializer(shortTerm, many = True)
        
        # LongTerm work queryset
        longTerm = LongTerm.objects.filter(
            Q(user = user) & Q(date__gte = start_date) & Q(date__lte = end_date)
        ) | LongTerm.objects.filter(
            Q(user = user) & Q(end_date__gte = start_date) & Q(end_date__lte = end_date)
        ) | LongTerm.objects.filter(
            Q(user = user) & Q(date__lte = start_date) & Q(end_date__gte = end_date)
        )

        longTermSerializer = LongTermSerializer(longTerm, many = True)

        ret = {
            'shortterm': shortTermSerializer.data,
            'longterm': longTermSerializer.data
        }

        return Response(ret)
    
    # POST
    def post(self, request):

        work_type = request.data.get('end_date', default = None)
        
        data = request.data.dict()
        data['status'] = 'O'

        serializer = None

        if work_type is None: serializer = ShortTermSerializer(data = data)
        else: serializer = LongTermSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ShortTermDetailAPI(APIView):
    # GET
    def get(self, request, uid):

        return Response(status=status.HTTP_400_BAD_REQUEST)

    # PUT
    def put(self, request, uid):

        return Response(status=status.HTTP_400_BAD_REQUEST)

    # DEL
    def delete(self, request, uid):

        return Response(status=status.HTTP_400_BAD_REQUEST)




class LongTermDetailAPI(APIView):
    # GET
    def get(self, request, uid):

        return Response(status=status.HTTP_400_BAD_REQUEST)

    # PUT
    def put(self, request, uid):

        return Response(status=status.HTTP_400_BAD_REQUEST)

    # DEL
    def delete(self, request, uid):

        return Response(status=status.HTTP_400_BAD_REQUEST)




class RepeatAPI(APIView):
    # GET
    def get(self, request, uid):

        return Response(status=status.HTTP_400_BAD_REQUEST)

    # PUT
    def put(self, request, uid):

        return Response(status=status.HTTP_400_BAD_REQUEST)

    # DEL
    def delete(self, request, uid):

        return Response(status=status.HTTP_400_BAD_REQUEST)