# Generated by Django 4.0.4 on 2022-06-03 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='names',
            name='number',
        ),
    ]
