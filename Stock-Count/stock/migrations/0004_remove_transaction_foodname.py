# Generated by Django 2.2.12 on 2020-04-26 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20200426_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='foodName',
        ),
    ]