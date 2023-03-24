from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import permissions, generics, mixins, status
from .serializers import SerailizerCompany, SerailizerUser
from .serializers import SerailizerStation, SerailizerUser
from .serializers import Serailizerisland, SerailizerUser
from .serializers import SerailizerTank, SerailizerUser
from .serializers import SerailizerPump, SerailizerUser
from .serializers import SerailizerNozzle, SerailizerUser
from .serializers import SerailizerMeters, SerailizerUser
from .serializers import SerailizerConsumption, SerailizerUser
from .serializers import SerailizerTechnician, SerailizerUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token
from .models import Company
from .models import Station
from .models import island
from .models import Tank
from .models import Pump
from .models import Nozzle
from .models import Meters
from .models import Consumption
from .models import Technician


# Create your views here.
class LoginUser(APIView):
    def post(self,request):
        if 'username' not in request.data or 'password' not in request.data:
            return Response({
                "msg":"Missing credential"
            },
            status = status.HTTP_400_BAD_REQUEST
            )
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            _,token = Token.objects.get_or_create(user=user)
            return Response({
                "token":token,
                "userData":request.data,    
            },
            status = status.HTTP_200_OK
            )
        return Response({
            "msg":"invalid credential"
        })


# class CompanyList(APIView):
#     def get(self,request):
#         company1= Company.objects.all()
#         serializer=SerailizerCompany(company1, many= True)
#         return Response(serializer.data)


#     def post(self):
#         pass

class getCompany(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class= SerailizerCompany
    serializer_classes= SerailizerCompany
    queryset= Company.objects.all()
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
    


class getisland(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class= Serailizerisland
    serializer_classes= Serailizerisland
    queryset= island.objects.all()
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
    




class getMeters(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class= SerailizerMeters
    serializer_classes= SerailizerMeters
    queryset= Meters.objects.all()
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
    
    
    

    
    
    
        


