# Generated by Django 5.0.4 on 2024-05-07 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventoryitem',
            old_name='catergorie',
            new_name='category',
        ),
    ]
