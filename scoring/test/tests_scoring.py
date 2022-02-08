from rest_framework.test import APITestCase
from scoring.models import Employee
from django.urls import reverse
from rest_framework import status

from scoring.views import EmployeesViewSet

class EmployeeTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("Employees-list")
        #print(self.list_url)
        self.employee_1= Employee.objects.create(
            includeAt = "2019-03-10 17:25:00", employeedId=123, employerId=789
        )
        self.employee_2= Employee.objects.create(
            includeAt = "2018-10-10 05:25:00", employeedId=213, employerId=123
        )
       
    #def test_fail(self):
    #    self.fail("Test Failed")
    def test_get_request(self):
        """ Test to check if the get request in working"""
        response= self.client.get(self.list_url)
        self.assertEquals(response.status_code,status.HTTP_200_OK )

    def test_post_request(self):
        """ Test to check if the POST request in working"""
        data={
            "includeAt" :"2015-03-03 07:25:00",
            "employeedId":241,
            "employerId":337

        }
        response= self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code,status.HTTP_201_CREATED )
    def test_django_view(self):
        """ Test to check if the django view request in working"""
        data={
            "includeAt" :"2015-03-03 07:25:00",
            "employeedId":241,
            "employerId":337

        }
        response= self.client.post("/send", data=data)
        self.assertEquals((response.content).decode("utf-8"),"Enviado" )
    
    
