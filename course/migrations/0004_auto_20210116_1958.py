# Generated by Django 3.1.5 on 2021-01-16 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_courses_course_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
    ]
