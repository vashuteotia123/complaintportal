# Generated by Django 2.2.5 on 2020-07-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Complaintapp', '0005_complaintinfo_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='wardeninfo',
            name='contact',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='wardeninfo',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
