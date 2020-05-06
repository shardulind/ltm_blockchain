# Generated by Django 3.0.3 on 2020-04-17 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicants_firstname', models.CharField(max_length=50)),
                ('applicants_middlename', models.CharField(max_length=50)),
                ('applicants_lastname', models.CharField(max_length=60)),
                ('applicants_mobno', models.CharField(max_length=12)),
                ('applicants_adharno', models.CharField(max_length=12)),
                ('survey_no', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
