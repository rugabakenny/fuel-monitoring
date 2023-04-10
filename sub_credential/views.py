from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import permissions, generics, mixins, status
from .serializers import SerailizerCompany, SerailizerUser
from .serializers import SerailizerStation, SerailizerUser
from .serializers import Serailizeriland, SerailizerUser
from .serializers import SerailizerTank, SerailizerUser
from .serializers import SerailizerPump, SerailizerUser
from .serializers import SerailizerNozzle, SerailizerUser
from .serializers import SerailizerMeters, SerailizerUser
from .serializers import SerailizerConsumption, SerailizerUser
from .serializers import SerailizerTechnician, SerailizerUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView #Apiview class
from rest_framework.response import Response #response
from .models import Company
from .models import Station
from .models import iland
from .models import Tank
from .models import Pump
from .models import Nozzle
from .models import Meters
from .models import Consumption
from .models import Technician


# Create your views here.


class LoginApi(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'userID': user.pk,
            'email': user.email,
            'first_name':user.first_name,
            'last_name':user.last_name

        })



class getCompany(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class= SerailizerCompany
    serializer_classes= SerailizerCompany
    queryset= Company.objects.all()

    def get(self, request):

        return self.list(request)

    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class getCompanyDetail(generics.GenericAPIView, mixins.ListModelMixin):
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        campany = self.get_object(pk)
        serializer = SerailizerCompany(campany)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = SerailizerCompany(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        campany = self.get_object(pk)
        campany.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class getStation(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class= SerailizerStation
    serializer_classes= SerailizerStation
    queryset= Station.objects.all()
    # lookup_field='id'
    def get(self, request):

        return self.list(request)
    
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    





class getStationDetail(generics.GenericAPIView, mixins.ListModelMixin):
    def get_object(self, pk):
        try:
            return Station.objects.get(pk=pk)
        except Station.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        station = self.get_object(pk)
        serializer = SerailizerStation(station)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = SerailizerStation(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        station = self.get_object(pk)
        station.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class getiland(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class= Serailizeriland
    serializer_classes= Serailizeriland
    queryset= iland.objects.all()
    # lookup_field='id'
    def get(self, request):

        return self.list(request)
    
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class getilandDetail(generics.GenericAPIView, mixins.ListModelMixin):
    def get_object(self, pk):
        try:
            return iland.objects.get(pk=pk)
        except iland.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        campany = self.get_object(pk)
        serializer = Serailizeriland(iland)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = Serailizeriland(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        iland = self.get_object(pk)
        iland.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class getTank(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class= SerailizerTank
    serializer_classes= SerailizerTank
    queryset= Tank.objects.all()
    # lookup_field='id'
    def get(self, request):

        return self.list(request)
    
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class getTankDetail(generics.GenericAPIView, mixins.ListModelMixin):
    def get_object(self, pk):
        try:
            return Tank.objects.get(pk=pk)
        except Tank.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tank = self.get_object(pk)
        serializer = SerailizerTank(tank)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = SerailizerTank(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tank = self.get_object(pk)
        tank.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class getPump(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class= SerailizerPump
    serializer_classes= SerailizerPump
    queryset= Pump.objects.all()
    # lookup_field='id'
    def get(self, request):

        return self.list(request)
    
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class getPumpDetail(generics.GenericAPIView, mixins.ListModelMixin):
    def get_object(self, pk):
        try:
            return Pump.objects.get(pk=pk)
        except Pump.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pump = self.get_object(pk)
        serializer = SerailizerPump(pump)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = SerailizerPump(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pump = self.get_object(pk)
        pump.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class getNozzle(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class= SerailizerNozzle
    serializer_classes= SerailizerNozzle
    queryset= Nozzle.objects.all()
    # lookup_field='id'
    def get(self, request):

        return self.list(request)
    
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class getNozzleDetail(generics.GenericAPIView, mixins.ListModelMixin):
    def get_object(self, pk):
        try:
            return Nozzle.objects.get(pk=pk)
        except Nozzle.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        nozzle = self.get_object(pk)
        serializer = SerailizerNozzle(nozzle)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = SerailizerNozzle(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        nozzle = self.get_object(pk)
        nozzle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class getMeters(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class= SerailizerMeters
    serializer_classes= SerailizerMeters
    queryset= Meters.objects.all()
    
    def get(self, request):

        return self.list(request)
    
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)





class getMetersDetail(generics.GenericAPIView, mixins.ListModelMixin):
    def get_object(self, pk):
        try:
            return Meters.objects.get(pk=pk)
        except Meters.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        meters = self.get_object(pk)
        serializer = SerailizerMeters(meters)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = SerailizerMeters(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        meters = self.get_object(pk)
        meters.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class getConsumption(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class= SerailizerConsumption
    serializer_classes= SerailizerConsumption
    queryset= Consumption.objects.all()
    # lookup_field='id'
    def get(self, request):

        return self.list(request)
    
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)





class getConsumptionDetail(generics.GenericAPIView, mixins.ListModelMixin):
    def get_object(self, pk):
        try:
            return Consumption.objects.get(pk=pk)
        except Consumption.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        consumption = self.get_object(pk)
        serializer = SerailizerConsumption(consumption)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = SerailizerConsumption(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        consumption = self.get_object(pk)
        consumption.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class getTechnician(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class= SerailizerTechnician
    serializer_classes= SerailizerTechnician
    queryset= Technician.objects.all()
    # lookup_field='id'
    def get(self, request):

        return self.list(request)
    
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class getTechnicianDetail(generics.GenericAPIView, mixins.ListModelMixin):
    def get_object(self, pk):
        try:
            return Technician.objects.get(pk=pk)
        except Technician.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        technician = self.get_object(pk)
        serializer = SerailizerTechnician(technician)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = SerailizerTechnician(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        technician = self.get_object(pk)
        technician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    

    
    
    
        


