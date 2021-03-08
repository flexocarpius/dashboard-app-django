# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def to_dict(self):
        return {
            'id': self.pk,
            'title': self.title,
            'icon': self.icon,
            'tasks': [task.to_dict() for task in self.task_set.all()]
        }

class Task(models.Model):
    content = models.CharField(max_length=1000)
    state = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def to_dict(self):
        return {
            'id': self.pk,
            'content': self.content,
            'state': self.state
        }

class Employee(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    salary = models.FloatField()

    def to_dict(self):
        return {
            'id': self.pk,
            'name': self.name,
            'country': self.country,
            'city': self.city,
            'salary': self.salary
        }
