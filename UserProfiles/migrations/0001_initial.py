# Generated by Django 2.2.5 on 2019-10-10 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=250)),
                ('travel_style', models.CharField(choices=[('FOODIE', 'Foodie'), ('LUX', 'Lux'), ('BUDGET', 'Budget'), ('SOLO', 'Solo'), ('HOTEL', 'Hotel'), ('FAMILY', 'Family'), ('WORK', 'Work')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
