# Generated by Django 3.2 on 2023-03-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_credential', '0011_auto_20230327_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='fueltype',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
