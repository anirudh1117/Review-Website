# Generated by Django 3.1.5 on 2021-01-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210121_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phoneNo',
            field=models.DecimalField(blank=True, decimal_places=0, default=None, max_digits=10),
        ),
    ]
