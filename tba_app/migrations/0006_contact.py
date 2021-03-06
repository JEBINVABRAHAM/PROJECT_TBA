# Generated by Django 3.0 on 2020-02-05 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tba_app', '0005_registration_expirydate'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('emailid', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=30)),
                ('msg', models.CharField(max_length=50)),
                ('status', models.CharField(blank=True, default='off', max_length=10, null=True)),
            ],
        ),
    ]
