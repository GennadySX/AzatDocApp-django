from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('api/category', ApiCategoriesView.as_view()),
    path('api/category_block', ApiBlockView.as_view()),
    path('api/theme', ApiThemeView.as_view()),
    path('api/detail', ApiDetailView.as_view()),

]
