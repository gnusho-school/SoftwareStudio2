from django.core import serializers
from rest_framework import serializers
from. models import ShortTerm, LongTerm

class ShortTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortTerm
        fields = '__all__'

class LongTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = LongTerm
        fields = '__all__'