from django.db import models
from user.models import Users

class Work(models.Model):
    
    title = models.CharField(max_length = 100)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    
    # 날짜 및 시간 처리
    date = models.DateField()

    # 달성, 미달성
    STATUS_CHOICES = (
        ('D', 'Done'),
        ('F', 'Failed'),
        ('O', 'Ongoing')
    )

    status = models.CharField(max_length = 1, choices = STATUS_CHOICES)

class ShortTerm(Work):
    
    start_time = models.TimeField()
    end_time =  models.TimeField()

class LongTerm(Work):
    
    end_date = models.DateField()