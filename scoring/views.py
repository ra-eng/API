import imp
from urllib import response
from django.http import HttpResponse
from rest_framework import viewsets
from scoring.models import Employee
from scoring.serializer import EmployeeSerializer
import requests
from collections import defaultdict

API_URL= "https://api.mockytonk.com/proxy/ab2198a3-cafd-49d5-8ace-baac64e72222"

class EmployeesViewSet(viewsets.ModelViewSet):
    """Showing all the Employees """
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer 
    listqueryset=queryset.values()

    def django_view(request):
        parsedict={}
        listqueryset= (Employee.objects.all()).values()
        for i in listqueryset:
            parsedict = defaultdict()
            parsedict["includeAt"]= i["includeAt"]
            parsedict["employeedId"]= i["employeedId"]
            parsedict["employerId"] = i["employerId"]
            r= requests.post(API_URL, data=parsedict)
            print(r)
        return HttpResponse("Enviado")



    
    

# Create your views here.
