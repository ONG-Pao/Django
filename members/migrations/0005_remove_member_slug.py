# Generated by Django 3.2.20 on 2023-09-06 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_member_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='slug',
        ),
    ]