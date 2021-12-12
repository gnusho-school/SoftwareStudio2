from django.db import models

class Users(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)

    uid = models.CharField(max_length = 30, db_index = True)
    #name = models.CharField(max_length = 30)
