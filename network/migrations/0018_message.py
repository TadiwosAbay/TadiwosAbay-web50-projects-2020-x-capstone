# Generated by Django 3.0.8 on 2020-08-29 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0017_auto_20200827_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('receiver', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=300)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
    ]