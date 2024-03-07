# Generated by Django 5.0.2 on 2024-03-05 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limonapp', '0004_advertisement_attributes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='category',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='limonapp.subcategory'),
        ),
    ]
