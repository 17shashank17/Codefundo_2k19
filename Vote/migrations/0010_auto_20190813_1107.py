# Generated by Django 2.1.1 on 2019-08-13 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0009_auto_20190813_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate_enrollment',
            name='candidate_pic',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='candidate_enrollment',
            name='logo',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
