# Generated by Django 4.2.6 on 2024-05-27 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_campaign_created_date_campaign_cemail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='sdate',
            field=models.DateField(auto_now_add=True, null='True'),
        ),
    ]
