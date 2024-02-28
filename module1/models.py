from django.db import models
from .forms import *
from django.db import models



# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    phonenumber=models.PositiveBigIntegerField()
    class Meta:
        db_table="Register"

class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')

class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    feedback=models.CharField(max_length=100)
    phonenumber=models.PositiveBigIntegerField()
    class Meta:
        db_table="feedback"
