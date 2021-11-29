from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.serializers import ALL_FIELDS
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Employee
from .serliazers import EmployeeSerializer


# Create your views here.
class EmployeeList(APIView):

    def get(self, request):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)
    
    
