# Generated by Django 2.1.1 on 2019-08-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0004_auto_20190812_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='voters_enrollment',
            name='voter_aadhar_pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]
