"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, JsonResponse
from app.models import Category, Employee, Task
import json
import random

def index(request):
    if Category.objects.all().count() == 0:
        restore_data()
    context = {
        'space': {
            'used': 25,
            'total': 50
        },
        'revenue': 23547.23,
        'fixed_issues': 45,
        'followers': 673,
        'employees': [employee.to_dict() for employee in Employee.objects.all()],
        'segment': 'index'
    };
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))

def reset(request):
    Employee.objects.all().delete()
    Category.objects.all().delete()
    Task.objects.all().delete()
    restore_data()
    return redirect("/")

def restore_data():
    # Create categories and tasks
    bugs = Category(title='Bugs', icon='bug_report')
    bugs.save()
    website = Category(title='Website', icon='code')
    website.save()
    server = Category(title='Server', icon='cloud')
    server.save()

    Task(content='Sign contract for "What are conference organizers afraid of?"', state=True, category=bugs).save()
    Task(content='Lines From Great Russian Literature? Or E-mails From My Boss?', state=True, category=bugs).save()
    Task(content='Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit', state=True, category=bugs).save()
    Task(content='Create 4 Invisible User Experiences you Never Knew About', state=True, category=bugs).save()
    
    Task(content='Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit', state=True, category=website).save()
    Task(content='Sign contract for "What are conference organizers afraid of?"', state=True, category=website).save()
    
    Task(content='Lines From Great Russian Literature? Or E-mails From My Boss?', state=True, category=server).save()
    Task(content='Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit', state=True, category=server).save()
    Task(content='Create 4 Invisible User Experiences you Never Knew About', state=True, category=server).save()

    Employee(name='Dakota Rice', country='Niger', city='Oud-Turnhout', salary=36738).save()
    Employee(name='Minerva Hooper', country='Curaçao', city='Sinaai-Waas', salary=23789).save()
    Employee(name='Sage Rodriguez', country='Netherlands', city='Baileux', salary=56142).save()
    Employee(name='Philip Chaney', country='Korea, South', city='Overland Park', salary=38735).save()
    Employee(name='Doris Greene', country='Malawi', city='Feldkirchen in Kärnten', salary=63542).save()
    Employee(name='Mason Porter', country='Chile', city='Gloucester', salary=78615).save()

# API Calls
def get_daily_sales(request):
    data = []
    for i in range(0, 7):
        value = random.randint(10, 50)
        data.append(value)
    return JsonResponse({'message': 'ok', 'data': data})

def get_email_subscriptions(request):
    data = []
    for i in range(0, 12):
        value = random.randint(100, 800)
        data.append(value)
    return JsonResponse({'message': 'ok', 'data': data})

def get_completed_tasks(request):
    data = []
    for i in range(0, 8):
        value = random.randint(100, 800)
        data.append(value)
    return JsonResponse({'message': 'ok', 'data': data}) 

def get_task_categories(request):
    categories = [category.to_dict() for category in Category.objects.all()]
    return JsonResponse({'message': 'ok', 'data': categories})

def delete_task(request):
    if (request.method == 'POST'):
        data = json.loads(request.body)
        if data.get('id', None) is not None:
            task = Task.objects.get(id=data.get('id'))
            if task is not None:
                task.delete()
                return JsonResponse({'message': 'ok', 'data': task.to_dict()});
            else:
                return JsonResponse({'message': 'Task not found.'});
        else:
            return JsonResponse({'message': 'Id not present.'});
    else:
        return JsonResponse({'message': 'Invalid method.'});

def update_task(request):
    if (request.method == 'POST'):
        data = json.loads(request.body)
        if data.get('id', None) is not None:
            task = Task.objects.get(id=data.get('id'))
            if task is not None:
                task.state = data.get('state', False)
                task.save()
                return JsonResponse({'message': 'ok', 'data': task.to_dict()});
            else:
                return JsonResponse({'message': 'Task not found.'});
        else:
            return JsonResponse({'message': 'Id not present.'});
    else:
        return JsonResponse({'message': 'Invalid method.'});