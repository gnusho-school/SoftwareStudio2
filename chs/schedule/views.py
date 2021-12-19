from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import Work, ShortTerm, LongTerm, Repeat
from .serializer import ShortTermSerializer, LongTermSerializer, RepeatSerializer
from user.models import Users
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime, timedelta
import json

# title = request.GET.get('title', None) -> query parameter 사용

def getShortTermQuerySet(user, start_date, end_date):
    ret = ShortTerm.objects.filter(
            Q(user = user) & Q(date__range = [start_date, end_date])
    )
    return ret

def getShortTermQuerySetRepeated(user, repeat, start_date, end_date):
    ret = ShortTerm.objects.filter(
            Q(user = user) & Q(repeat = repeat) & Q(date__range = [start_date, end_date])
    )
    return ret

def getLongTermQuerySet(user, start_date, end_date):
    ret = LongTerm.objects.filter(
        Q(user = user) & (
            (Q(date__gte = start_date) & Q(date__lte = end_date))|
            (Q(end_date__gte = start_date) & Q(end_date__lte = end_date))|
            (Q(date__lte = start_date) & Q(end_date__gte = end_date))|
            (Q(date__gte = start_date) & Q(end_date__lte = end_date))
        )
    )
    return ret

def getRepeatTermQuerySet(user, start_date, end_date):
    ret = Repeat.objects.filter(
        Q(user = user) & (
            (Q(start_date__gte = start_date) & Q(start_date__lte = end_date))|
            (Q(end_date__gte = start_date) & Q(end_date__lte = end_date))|
            (Q(start_date__lte = start_date) & Q(end_date__gte = end_date))|
            (Q(start_date__gte = start_date) & Q(end_date__lte = end_date))
        )
    )
    return ret

class WorkListAPI(APIView):
    # GET
    def get(self, request):
        
        user = request.GET.get('user', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        
        if user is None or start_date is None or end_date is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        # ShortTerm work queryset (includes repeat job)
        shortTerm = getShortTermQuerySet(user, start_date, end_date)
        
        shortTermSerializer = ShortTermSerializer(shortTerm, many = True)
        
        # LongTerm work queryset
        longTerm = getLongTermQuerySet(user, start_date, end_date)

        longTermSerializer = LongTermSerializer(longTerm, many = True)

        ret = {
            'shortterm': shortTermSerializer.data,
            'longterm': longTermSerializer.data
        }

        return Response(ret)
    
    # POST
    def post(self, request):

        return Response("Wrong URL", status=status.HTTP_400_BAD_REQUEST)

# SHORTTERM
class ShortTermListAPI(APIView):
    # GET
    def get(self, request):

        user = request.GET.get('user', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        
        if user is None or start_date is None or end_date is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        # ShortTerm work queryset (includes repeat job)
        shortTerm = getShortTermQuerySet(user, start_date, end_date)
        
        shortTermSerializer = ShortTermSerializer(shortTerm, many = True)

        ret = shortTermSerializer.data

        return Response(ret)
    
    # POST
    def post(self, request):

        print(request.data)
        data = request.data["data"]
        data['status'] = 'O'
        print(data)
        serializer = ShortTermSerializer(data = data)
        print(serializer)
        print(type(data['user']))
        print(serializer.is_valid())

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShortTermDetailAPI(APIView):
    # GET
    def get(self, request, pk):

        shortterm = get_object_or_404(ShortTerm, pk = pk)
        serializer = ShortTermSerializer(shortterm)

        return Response(serializer.data)

    # PUT
    def put(self, request, pk):

        shortterm = get_object_or_404(ShortTerm, pk = pk)
        serializer = ShortTermSerializer(shortterm, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DEL
    def delete(self, request, pk):
        shortterm = get_object_or_404(ShortTerm, pk = pk)
        shortterm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# LONGTERM
class LongTermListAPI(APIView):
    # GET
    def get(self, request):

        user = request.GET.get('user', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        
        if user is None or start_date is None or end_date is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        # LongTerm work queryset
        longTerm = getLongTermQuerySet(user, start_date, end_date)

        longTermSerializer = LongTermSerializer(longTerm, many = True)

        ret = longTermSerializer.data

        return Response(ret)
    
    # POST
    def post(self, request):

        data = request.data['data']
        data['status'] = 'O'
        serializer = LongTermSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LongTermDetailAPI(APIView):
    # GET
    def get(self, request, pk):

        longterm = get_object_or_404(LongTerm, pk = pk)
        serializer = LongTermSerializer(longterm)

        return Response(serializer.data)

    # PUT
    def put(self, request, pk):

        longterm = get_object_or_404(LongTerm, pk = pk)
        serializer = LongTermSerializer(longterm, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DEL
    def delete(self, request, pk):
        longterm = get_object_or_404(LongTerm, pk = pk)
        longterm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# REPEAT
class RepeatListAPI(APIView):
    # GET
    def get(self, request):
        
        user = request.GET.get('user', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)

        if user is None or start_date is None or end_date is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        # repeat list
        repeat = getRepeatTermQuerySet(user, start_date, end_date)
        repeatSerializer = RepeatSerializer(repeat, many = True)

        # shorterms per repeat
        id_list = [x['id'] for x in repeatSerializer.data]
        shortTerms = []
        
        for idx in id_list:
            tmp = getShortTermQuerySetRepeated(user, idx, start_date, end_date)
            shortTermsSerializer = ShortTermSerializer(tmp, many = True)
            shortTerms.append({
                'repeat_id': idx,
                'shortterms': shortTermsSerializer.data
            })

        ret = {
            'repeat': repeatSerializer.data,
            'shortTerms': shortTerms
        }

        return Response(ret)
    
    # POST
    def post(self, request):
        
        serializer = RepeatSerializer(data = request.data)
        if serializer.is_valid():

            serializer.save()

            repeat = serializer.data['id']

            data = request.data.dict()
            
            day = datetime.strptime(data['start_date'], '%Y-%m-%d')
            limit = datetime.strptime(data['end_date'], '%Y-%m-%d')
            term = int(data['term'])

            title = data['title']
            start_time = data['start_time'] if 'start_time' in data else None
            end_time = data['end_time'] if 'end_time' in data else None
            user = int(data['user'])
            
            shortTerm = {
                'title': title,
                'user': user,
                'date': day,
                'repeat': repeat,
                'status': 'O'
            }

            if start_time is not None: shortTerm['start_time'] = start_time
            if end_time is not None: shortTerm['end_time'] = end_time

            shortTerms = []

            while day <= limit:
                
                shortTerm['date'] = day.strftime("%Y-%m-%d")
                serializer_ = ShortTermSerializer(data = shortTerm)
        
                if serializer_.is_valid():
                    serializer_.save()
                    shortTerms.append(serializer_.data) 

                day += timedelta(days = term)
            
            ret = {
                'repeat': serializer.data,
                'shortterms': shortTerms
            }

            return Response(ret, status = 200)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class RepeatDetailAPI(APIView):
    # GET
    def get(self, request, pk):

        repeat = get_object_or_404(Repeat, pk = pk)

        serializer = RepeatSerializer(repeat)

        user = request.GET.get('user', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)

        if user is None or start_date is None or end_date is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        shortTerms = getShortTermQuerySetRepeated(user, pk, start_date, end_date)

        shortTermsSerializer = ShortTermSerializer(shortTerms, many = True)

        ret = shortTermsSerializer.data

        return Response(ret)

    # PUT
    def put(self, request, pk):

        return Response(status=status.HTTP_400_BAD_REQUEST)

    # DEL
    def delete(self, request, pk):

        repeat = get_object_or_404(Repeat, pk = pk)
        repeat.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)