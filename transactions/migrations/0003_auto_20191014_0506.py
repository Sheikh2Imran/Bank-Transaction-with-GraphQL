# Generated by Django 2.2.6 on 2019-10-14 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20191013_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='user',
            new_name='account',
        ),
    ]
