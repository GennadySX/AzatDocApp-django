from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import  redirect
from django.template import RequestContext
from .models import *
from rest_framework import generics
from .serializers import *


# Create your views here.

# Create your views here.


class ApiCategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer

class ApiBlockView(generics.ListCreateAPIView):
    queryset = CategoryBlock.objects.all()
    serializer_class = CategoryBlockSerializer


class ApiThemeView(generics.ListCreateAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


class ApiDetailView(generics.ListCreateAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
