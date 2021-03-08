# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from . import views

app_name='app'

urlpatterns = [
    path('', views.index, name='index'),
    path('reset/', views.reset, name='reset'),
    path('categories/', views.get_task_categories, name='get_categories'),
    path('delete/', views.delete_task, name='delete_task'),
    path('update/', views.update_task, name='update_task'),
    path('email_subscriptions/', views.get_email_subscriptions, name='email_subscriptions'),
    path('completed_tasks/', views.get_completed_tasks, name='completed_tasks'),
    path('daily_sales/', views.get_daily_sales, name='daily_sales'),
]
