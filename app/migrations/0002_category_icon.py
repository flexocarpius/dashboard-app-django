# Generated by Django 3.1.5 on 2021-01-19 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(default='bug_report', max_length=100),
            preserve_default=False,
        ),
    ]
