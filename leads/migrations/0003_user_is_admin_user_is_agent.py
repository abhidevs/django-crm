# Generated by Django 4.0 on 2022-07-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_organisation_agent_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
    ]
