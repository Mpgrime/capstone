# Generated by Django 4.2.6 on 2023-12-04 20:14

import account.models
import account.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_first_member_name_remove_member_last_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='about',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='member',
            name='pic',
            field=models.ImageField(default='default/blankprof.png', storage=account.storage.OverwriteStorage(), upload_to=account.models.user_directory_profile),
        ),
    ]
