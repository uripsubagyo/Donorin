# Generated by Django 4.1.2 on 2022-11-02 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_alter_news_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='user',
        ),
    ]
