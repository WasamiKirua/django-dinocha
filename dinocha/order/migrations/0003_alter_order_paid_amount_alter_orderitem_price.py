# Generated by Django 4.1.7 on 2023-03-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0002_alter_order_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="paid_amount",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="price",
            field=models.FloatField(),
        ),
    ]
