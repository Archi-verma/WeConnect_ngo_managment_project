# Generated by Django 4.2.6 on 2024-05-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NGO_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20, null='False')),
                ('confirm_password', models.CharField(max_length=20, null='False')),
                ('mission', models.CharField(max_length=100, null='True')),
                ('area', models.CharField(choices=[('Education', 'Education'), ('Healthcare', 'Healthcare'), ('Environment', 'Environment'), ('Human Right', 'Human Right')], max_length=20)),
            ],
        ),
    ]
