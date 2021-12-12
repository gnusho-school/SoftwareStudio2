from django.core import serializers
from rest_framework import serializers
from. models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'