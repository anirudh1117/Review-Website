# Generated by Django 3.1.5 on 2021-01-16 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20210117_0238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_table',
            name='phone',
        ),
    ]