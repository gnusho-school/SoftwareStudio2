from django.shortcuts import render
from django.http import HttpResponse
from .models import Work, ShortTerm, LongTerm
from user.models import Users
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

