# Generated by Django 2.2.7 on 2019-11-09 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_userinfo_parameters'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='jsonparams',
            new_name='params',
        ),
    ]
