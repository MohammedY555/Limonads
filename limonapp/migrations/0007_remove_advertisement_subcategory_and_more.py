# Generated by Django 5.0.2 on 2024-03-05 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limonapp', '0006_alter_advertisement_advertise_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='limonapp.category'),
        ),
    ]