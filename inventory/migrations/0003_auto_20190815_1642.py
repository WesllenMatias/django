# Generated by Django 2.2 on 2019-08-15 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_controleti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controleti',
            name='Ip_Address',
            field=models.CharField(max_length=18),
        ),
    ]
