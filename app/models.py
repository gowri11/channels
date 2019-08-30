from django.db import models
class Register(models.Model):
    name=models.CharField(max_length=20)
    area=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.CharField(max_length=20)


class Dishes(models.Model):
    MY_CHOICES = [('m','maatv'),('z','zeetv'),('e','etv'),('s','sony'),('b','bhakti tv'),('n','ntv')]
    viewer_name=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)
    email=models.EmailField()
    amount=models.CharField(max_length=20)
    recharge_date=models.CharField(max_length=20)
    expire_date=models.CharField(max_length=20)
    select_channel=models.CharField(max_length=20,choices=MY_CHOICES)
    # def__str__(self):
    #     return self.viewer_name

# class Airtel(models.Model):
#     viewer= models.ForeignKey(Register, on_delete=models.CASCADE)
#      Channel = models.()
     
# Create your models here.
