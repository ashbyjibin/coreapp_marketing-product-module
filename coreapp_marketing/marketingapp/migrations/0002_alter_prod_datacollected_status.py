# Generated by Django 3.2.10 on 2022-01-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketingapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prod_datacollected',
            name='status',
            field=models.BooleanField(null=True),
        ),
    ]
