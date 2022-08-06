# Generated by Django 3.2.6 on 2022-08-04 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RevenueHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('purchase_code', models.CharField(max_length=500, null=True, verbose_name='Purchase Refer')),
                ('product_name', models.CharField(max_length=500, null=True, verbose_name='Purchase Refer')),
                ('purchase_unit', models.FloatField(null=True)),
                ('selling_unit', models.FloatField(null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('profits', models.FloatField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Revenue History',
            },
        ),
    ]
