from django.db import models

# Create your models here.
class Listing(models.Model):
    lab_name=models.CharField(max_length=100,default="")
    systems=models.IntegerField(blank=True, null=True,default=0)
    monm=models.CharField(max_length=100,blank=True, null=True,default="")
    mone=models.CharField(max_length=100,blank=True, null=True,default="")
    tuem=models.CharField(max_length=100,blank=True, null=True,default="")
    tuee=models.CharField(max_length=100,blank=True, null=True,default="")
    wedm=models.CharField(max_length=100,blank=True, null=True,default="")
    wede=models.CharField(max_length=100,blank=True, null=True,default="")
    thum=models.CharField(max_length=100,blank=True, null=True,default="")
    thue=models.CharField(max_length=100,blank=True, null=True,default="")
    frim=models.CharField(max_length=100,blank=True, null=True,default="")
    frie=models.CharField(max_length=100,blank=True, null=True,default="")
    satm=models.CharField(max_length=100,blank=True, null=True,default="")
    sate=models.CharField(max_length=100,blank=True, null=True,default="")
