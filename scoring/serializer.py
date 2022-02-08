import imp
from rest_framework import serializers
from scoring.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Employee
        fields= "__all__"

