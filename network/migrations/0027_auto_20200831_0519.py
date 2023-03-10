# Generated by Django 3.0.8 on 2020-08-31 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0026_auto_20200831_0517'),
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
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='courseregistered',
            name='student',
            field=models.CharField(max_length=100),
        ),
    ]
