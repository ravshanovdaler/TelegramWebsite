# Generated by Django 4.2.7 on 2023-11-01 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_infomodel_mijozlar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mijozlar',
            new_name='Clients',
        ),
    ]
