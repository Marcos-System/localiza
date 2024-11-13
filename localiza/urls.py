from django.urls import path
from localiza.views import *
from django.conf.urls import handler404
from django.shortcuts import redirect

urlpatterns = [

    path("", polos, name="polos"),


]

