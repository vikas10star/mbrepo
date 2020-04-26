from rest_framework import viewsets
from . import serializers
from . import models

class EmployeeViewset(viewsets.ModelViewSet):
	queryset = models.Employee.objects.all()
	serializer_class = serializers.EmployeeSerializer
