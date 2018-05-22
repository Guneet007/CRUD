from django.contrib.auth.models import User
from .models import Student
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('student_id','username', 'first_name', 'last_name', 'college','branch')
