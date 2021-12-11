from django.db import models

class Schedule(models.Model):
    title = models.CharField(max_length = 100)
    '''
    type = 
    start_date = 
    end_date =
    start_time =
    end_time = 
    status =
    '''

    def __str__(self):
        return f'[{self.pk}]{self.title}'