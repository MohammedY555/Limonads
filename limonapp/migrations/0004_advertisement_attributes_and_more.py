# Generated by Django 5.0.2 on 2024-03-05 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limonapp', '0003_advertisementattribute_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='attributes',
            field=models.ManyToManyField(through='limonapp.AdvertisementAttribute', to='limonapp.attribute'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='limonapp.category'),
        ),
    ]