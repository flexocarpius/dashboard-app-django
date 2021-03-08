# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from . import views

app_name='app'

urlpatterns = [
    path('', views.index, name='index')
]
