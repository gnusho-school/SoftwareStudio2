"""chs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.WorkListAPI.as_view()),
    path('shorterm/<int:pk>/', views.ShortTermDetailAPI.as_view()),
    path('longterm/<int:pk>/', views.LongTermDetailAPI.as_view()),
    path('repeat/', views.RepeatAPI.as_view()),
]

'''
대전제: query parameter로 user의 pk와 start_date + end_date가 "%y-%m-%d"의 형태로 전달됨
1. GET ShortTerm과 LongTerm 합친 모든 work 
(GET "base_url/schedule/?user=<pk>&start_date=<date>&end_date=date")
2. POST ShortTerm과 LongTerm 합친 모든 work
(POST "base_url/schedule/") -> body에 내용 추가
'''