# Generated by Django 2.1.1 on 2019-08-12 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.CharField(blank=True, max_length=20000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='candidate_enrollment',
            name='aadhar_no',
            field=models.CharField(max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='voters_enrollment',
            name='aadhar_no',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
