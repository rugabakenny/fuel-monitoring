# Generated by Django 3.2 on 2023-03-27 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_credential', '0010_auto_20230327_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='companyrotation',
        ),
        migrations.RemoveField(
            model_name='company',
            name='companystaff',
        ),
        migrations.RemoveField(
            model_name='company',
            name='companystation',
        ),
        migrations.RemoveField(
            model_name='company',
            name='stationmanagers',
        ),
    ]
