# Generated by Django 4.1.7 on 2023-03-21 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"ordering": ("-created_at",)},
        ),
    ]
