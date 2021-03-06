# Generated by Django 4.0 on 2022-07-19 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=50)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='leads.user')),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='organisation',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='leads.organisation'),
            preserve_default=False,
        ),
    ]
