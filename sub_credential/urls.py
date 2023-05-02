from django.urls import include, path
from rest_framework import routers
from . views import LoginApi, getCompany ,getCompanyDetail, getStation , getStationDetail , getiland , getilandDetail , getTank , getTankDetail ,getPump , getPumpDetail ,getNozzle ,getNozzleDetail , getMeters , getMetersDetail , getConsumption , getConsumptionDetail , getTechnician , getTechnicianDetail


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('login/',LoginApi.as_view()),
    path('getcompanys/',getCompany.as_view()),
    path('getcompany/<int:pk>/',getCompanyDetail.as_view()),
    path('getstations/',getStation.as_view()),
    path('getstation/<int:pk>/',getStationDetail.as_view()),
    path('getilands/',getiland.as_view()),
    path('get /<int:pk>/',getilandDetail.as_view()),
    path('gettanks/',getTank.as_view()),
    path('gettank/<int:pk>/',getTankDetail.as_view()),
    path('getpumps/',getPump.as_view()),
    path('getpump/<int:pk>/',getPumpDetail.as_view()),
    path('getnozzles/',getNozzle.as_view()),
    path('getnozzle/<int:pk>/',getNozzleDetail.as_view()),
    path('getmeters/',getMeters.as_view()),
    path('getmeter/<int:pk>/',getMetersDetail.as_view()),
    path('getconsumptions/',getConsumption.as_view()),
    path('getconsumption/<int:pk>/',getConsumptionDetail.as_view()),
    path('gettechnicians/',getTechnician.as_view()),
    path('gettechnician/<int:pk>/',getTechnicianDetail.as_view()),
]