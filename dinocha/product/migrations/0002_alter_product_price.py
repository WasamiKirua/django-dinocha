# Generated by Django 4.1.7 on 2023-03-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.FloatField(),
        ),
    ]
