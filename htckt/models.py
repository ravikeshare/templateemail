from django.db import models
from django.utils import timezone
from decimal import Decimal
from django.core.validators import RegexValidator
# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '9999999999'. Up to 15 digits allowed.")
    phone = models.CharField(max_length=50)#models.CharField(validators=[phone_regex], max_length = 15, blank=False) # validators should be a list
    reg_date = models.CharField(max_length=50)
    institute_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=50)
    passing_yr = models.CharField(max_length=4)
    agg_10th_percntge = models.CharField(max_length=50)
    agg_12th_percntge = models.CharField(max_length=50)
    agg_BE_percntge = models.CharField(max_length=50)
    tpo_email = models.EmailField(max_length=80)
    status = models.BooleanField(default=False)
    position =  models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return u"%s - %s - %s" % (self.first_name, self.last_name, self.institute_name)


from import_export import resources



class StudentResource(resources.ModelResource):

    class Meta:
        model = Student

