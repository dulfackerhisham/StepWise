# Generated by Django 4.2.3 on 2023-11-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0016_alter_order_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("out for shipping", "out for shipping"),
                    ("completed", "completed"),
                    ("pending", "pending"),
                ],
                default="Pending",
                max_length=150,
            ),
        ),
    ]
