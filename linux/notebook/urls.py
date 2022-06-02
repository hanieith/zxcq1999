from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('view/', view_names, name='view'),
]