from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
# Create your models here.
class Accountuser(models.Model): 
    ACCOUNT_TYPE_CHOICES = [
        ('company_admin', 'company_admin'),
        ('company_staff', 'company_staff'),
        ('company_techinician', 'company_techinician'),
        ('station_manager', 'station_manager'),
        ('station_dispenser', 'station_dispenser'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phonenumber = models.IntegerField(null=True,default="-")
    usertype = models.CharField(null=True, max_length=255, choices=ACCOUNT_TYPE_CHOICES)
    accountstatus = models.CharField(null=True,max_length=255)

    

class Company(models.Model):
    companyname = models.CharField(null=True,max_length=255)
    companyaddress = models.CharField(null=True,max_length=255)
    phonenumber = models.IntegerField(default="-",null=True)
    companystatus = models.CharField(max_length=255,null=True)
    usertype = models.ForeignKey(User,on_delete=models.CASCADE)
    


    def __str__(self):
        return self.companyname




class Technician(models.Model):
    name = models.CharField(max_length = 255 ,null=True)  
    companyname = models.CharField(max_length = 255 ,null=True)  

    def __str__(self):
        return self.name
    
    
class Station(models.Model):
    stationname = models.CharField(max_length=255)
    companyid = models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.stationname
    

    

class iland(models.Model):
    ilandname = models.CharField(null=True,max_length=255)
    stationid = models.ForeignKey(Station,on_delete=models.CASCADE)
   
    

    def __str__(self):
        return self.ilandname

class Tank(models.Model):
    tankname = models.CharField(max_length=255,null=True)
    fueltype = models.CharField(max_length=255,null=True)
    
    
    

    def __str__(self):
        return self.tankname

class Pump(models.Model):
    pumpname = models.CharField(null=True,max_length=255)
    ilandid = models.ForeignKey(iland,on_delete=models.CASCADE)
   


    def __str__(self):
        return self.pumpname
    
class Nozzle(models.Model):
    nozzlename = models.CharField(max_length=255,null=True)
    fueltype = models.CharField(max_length=255, null=True)
    pumpid = models.ForeignKey(Pump,on_delete=models.CASCADE)
    tankid = models.ForeignKey(Tank,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nozzlename
    


class Meters(models.Model):
    metername = models.CharField(max_length = 255 ,null=True)
    type = models.CharField(max_length=255,null=True)
    tankid = models.ForeignKey(Tank,on_delete=models.CASCADE)
    status = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.metername
    
class Consumption(models.Model):
    meterid = models.ForeignKey(Meters,on_delete=models.CASCADE)
    meter_volume = models.CharField(max_length=255,null=True)

 