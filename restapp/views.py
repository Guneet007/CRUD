from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from .models import Student
from restapp.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        users = Student.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if(serializer.initial_data['username'].isdigit()):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_objectid(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    @staticmethod
    def get_object(emp_id):
        try:
            return Student.objects.get(username=emp_id)
        except Student.DoesNotExist:
            raise Http404

    @staticmethod
    def get_objectid(emp_id):
        try:
            print('*'*100)
            return Student.objects.get(pk=emp_id)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, emp_id, format=None):
        print(type(emp_id))
        if emp_id.isdigit():
            print('.'*100)
            user = self.get_objectid(emp_id)
        else:
            user = self.get_object(emp_id)
        user = UserSerializer(user)
        return Response(user.data)

    """def get(self, request, pk, format=None):
        user = self.get_objectid(pk)
        user = UserSerializer(user)
        return Response(user.data)"""

    def put(self, request, emp_id, format=None):
        user = self.get_object(emp_id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, emp_id, format=None):
        user = self.get_objectid(emp_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.
