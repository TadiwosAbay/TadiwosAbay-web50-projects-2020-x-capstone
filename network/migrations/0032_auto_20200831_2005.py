# Generated by Django 3.0.8 on 2020-08-31 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0031_auto_20200831_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coursefers', to='network.Teacher'),
        ),
        migrations.AlterField(
            model_name='courseregistered',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='googlers', to='network.Teacher'),
        ),
    ]
