# Generated by Django 4.1 on 2022-11-01 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='blood_group',
            field=models.CharField(max_length=3),
        ),
    ]