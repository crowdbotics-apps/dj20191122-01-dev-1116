# Generated by Django 2.2.7 on 2019-11-22 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customtext",
            name="dada",
            field=models.DecimalField(
                blank=True, decimal_places=10, max_digits=30, null=True
            ),
        ),
    ]
