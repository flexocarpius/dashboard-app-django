# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, include

urlpatterns = [
    path('', include('app.views.dashboard.urls', namespace='dashboard')),
    path('employees/', include('app.views.employees.urls', namespace='employees')),
]
