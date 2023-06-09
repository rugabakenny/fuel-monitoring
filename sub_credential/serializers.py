from . models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Company
from . models import Station
from .models import iland
from .models import Tank
from .models import Pump
from .models import Nozzle
from .models import Meters
from .models import Consumption
from .models import Technician


class SerailizerUser(serializers.ModelSerializer):
    model = User
    fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined','phonenumber','usertype','accountstatus')                                              



class SerailizerCompany(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'usertype', 'companystatus', 'companyname', 'companyaddress', 'phonenumber',]



class SerailizerStation(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = "__all__"


class Serailizeriland(serializers.ModelSerializer):
    class Meta:
        model = iland
        fields = "__all__"

class SerailizerTank(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = "__all__"

class SerailizerPump(serializers.ModelSerializer):
    class Meta:
        model =Pump
        fields = "__all__"


class SerailizerNozzle(serializers.ModelSerializer):
    class Meta:
        model =Nozzle
        fields = "__all__"

class SerailizerMeters(serializers.ModelSerializer):
    class Meta:
        model =Meters
        fields = "__all__"

class SerailizerConsumption(serializers.ModelSerializer):
    class Meta:
        model =Consumption
        fields = "__all__"

class SerailizerTechnician(serializers.ModelSerializer):
    class Meta:
        model =Technician
        fields = "__all__"




