# Generated by Django 4.2.6 on 2024-05-28 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_campaign_sdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='ngoid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.ngo_info'),
        ),
    ]
