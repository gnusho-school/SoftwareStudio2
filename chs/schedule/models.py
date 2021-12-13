from django.db import models
from user.models import Users

STATUS_CHOICES = (
        ('D', 'Done'),
        ('F', 'Failed'),
        ('O', 'Ongoing')
)

class Work(models.Model):
    
    title = models.CharField(max_length = 100)
    
    user = models.ForeignKey(
        Users, 
        on_delete = models.CASCADE
    )
    
    date = models.DateField()

    status = models.CharField(
        max_length = 1, 
        choices = STATUS_CHOICES
    )

    class Meta:
        abstract = True

class Repeat(models.Model):

    user = models.ForeignKey(
        Users, 
        on_delete = models.CASCADE
    )

    start_date = models.DateField()
    end_date = models.DateField()
    term = models.IntegerField()
    start_time = models.TimeField(null = True)
    end_time = models.TimeField(null = True)

class ShortTerm(Work):
    
    repeat = models.ForeignKey(
        Repeat, 
        on_delete = models.CASCADE,
        null = True 
    )
    start_time = models.TimeField(null = True)
    end_time =  models.TimeField(null = True)

class LongTerm(Work):
    
    end_date = models.DateField()