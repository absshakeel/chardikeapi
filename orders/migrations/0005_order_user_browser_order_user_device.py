# Generated by Django 4.0.5 on 2022-08-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_coupon_coupon_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_browser',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='user_device',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
