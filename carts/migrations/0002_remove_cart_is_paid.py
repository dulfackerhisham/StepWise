# Generated by Django 4.2.3 on 2023-09-05 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("carts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="is_paid",
        ),
    ]
