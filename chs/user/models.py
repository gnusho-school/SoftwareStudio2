from django.db import models

class User(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)

    uid = models.CharField(max_length = 30, primary_key = True)
    name = models.CharField(max_length = 30)

    def __str__(self):
        return f'[{self.name}]{self.pk}'
