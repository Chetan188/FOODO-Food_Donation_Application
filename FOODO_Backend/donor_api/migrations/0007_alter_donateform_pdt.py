# Generated by Django 3.2.7 on 2021-12-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor_api', '0006_donateform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donateform',
            name='pdt',
            field=models.CharField(max_length=200),
        ),
    ]