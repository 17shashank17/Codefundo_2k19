# Generated by Django 2.1.1 on 2019-08-18 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0019_auto_20190818_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voters_enrollment',
            name='mobile',
        ),
    ]