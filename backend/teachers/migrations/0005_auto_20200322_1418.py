# Generated by Django 3.0.3 on 2020-03-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_auto_20200321_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='description',
            field=models.CharField(default='description', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classes',
            name='number',
            field=models.IntegerField(default=123, unique=True),
            preserve_default=False,
        ),
    ]