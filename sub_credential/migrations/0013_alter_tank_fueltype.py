# Generated by Django 3.2 on 2023-03-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_credential', '0012_alter_tank_fueltype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='fueltype',
            field=models.CharField(max_length=255, null=True),
        ),
    ]