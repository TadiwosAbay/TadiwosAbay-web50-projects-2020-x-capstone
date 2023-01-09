# Generated by Django 3.0.8 on 2020-08-31 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0029_auto_20200831_0526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='read',
        ),
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
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smarts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boomers', to=settings.AUTH_USER_MODEL),
        ),
    ]
