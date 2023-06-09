# Generated by Django 3.2 on 2023-03-21 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sub_credential', '0003_rename_companyid_station_companyid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='companyID',
            new_name='companyid',
        ),
        migrations.CreateModel(
            name='Systemadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.IntegerField(default='-', null=True)),
                ('usertype', models.CharField(max_length=255, null=True)),
                ('accountstatus', models.CharField(max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
