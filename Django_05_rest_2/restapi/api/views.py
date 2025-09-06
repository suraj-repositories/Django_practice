from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer


# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['GET'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            employees = Employee.objects.filter(company=company)
            serializer = EmployeeSerializer(employees, many=True, context={'request': request})
            return Response(serializer.data)
        except Company.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer