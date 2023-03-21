from django.urls import include, path
from rest_framework import routers
from . views import LoginUser, getCompany , getStation ,getisland ,getTank , getPump ,getNozzle ,getMeters ,getConsumption


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('',LoginUser.as_view(),name="login"),
    path('getcompany/',getCompany.as_view()),
    path('getstation/',getStation.as_view()),
    path('getisland/',getisland.as_view()),
    path('gettank/',getTank.as_view()),
    path('getpump/',getPump.as_view()),
    path('getnozzle/',getNozzle.as_view()),
    path('getmeters/',getMeters.as_view()),
    path('getconsumption/',getConsumption.as_view()),
]