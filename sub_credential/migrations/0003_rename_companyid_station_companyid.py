# Generated by Django 3.2 on 2023-03-16 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_credential', '0002_company_island_tank_station_pump_nozzle_meters_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='companyid',
            new_name='companyID',
        ),
    ]
