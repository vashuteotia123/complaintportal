# Generated by Django 2.2.5 on 2020-07-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Complaintapp', '0008_auto_20200727_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='wardeninfo',
            name='block',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
