import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from randomtimestamp import randomtimestamp
import random
from scoring.models import Employee


def criando_pessoas(quantidade_de_pessoas):
    for _ in range(quantidade_de_pessoas):
        includeAt="{}".format(randomtimestamp(start_year=1700, end_year=2022, text=True,pattern = "%Y-%m-%d %I:%M:%S"))
        employeedId = "{}".format(random.randrange(1, 999))
        employerId= "{}".format(random.randrange(1, 999))
        print(includeAt)
        p = Employee(includeAt=includeAt, employeedId=employeedId, employerId=employerId)
        p.save()

criando_pessoas(10)