# Generated by Django 3.1.5 on 2021-01-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210121_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phoneNo',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]
