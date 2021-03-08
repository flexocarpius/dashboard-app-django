"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, JsonResponse
from app.models import Category, Employee, Task

def index(request):
    context = {
        'employees': [employee.to_dict() for employee in Employee.objects.all()],
        'segment': 'employees'
    };
    html_template = loader.get_template('employees/index.html')
    return HttpResponse(html_template.render(context, request))
