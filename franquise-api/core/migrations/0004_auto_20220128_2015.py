# Generated by Django 3.2.11 on 2022-01-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220128_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listfranchise',
            name='valuexquantity',
        ),
        migrations.AddField(
            model_name='listfranchise',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listfranchise',
            name='value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
