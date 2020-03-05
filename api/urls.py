from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *


urlpatterns = [
    path('api/category', ApiCategoriesView.as_view()),
    path('api/category_block', ApiBlockView.as_view()),
    path('api/theme', ApiThemeView.as_view()),
    url(r'^api/theme/(?P<theme_id>\d+)/$', ApiThemeByIDView.index, name='index'),
    path('api/detail', ApiDetailView.as_view()),

]
