# Generated by Django 3.0.7 on 2020-09-11 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20200911_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.CharField(default=9, max_length=9),
            preserve_default=False,
        ),
    ]
