import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudFBVproject.settings')
import django
django.setup()


from crudApp.models import *
from faker import Faker
from random import *
faker = Faker()


def populate(n):
    for i in range(n):
        feno = randint(1001,9999)
        fesal = randint(10000,20000)
        fename = faker.name()
        feaddr = faker.city()
        emp_record = Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)

populate(20)
