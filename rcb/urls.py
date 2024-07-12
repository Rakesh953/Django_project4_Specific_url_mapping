from django.urls import path
from rcb.views import *
app_name='byebye'

urlpatterns=[
    path('kohli',kohli,name='kohli')
] 