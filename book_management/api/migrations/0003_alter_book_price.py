# Generated by Django 4.1.6 on 2023-03-19 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="price",
            field=models.CharField(max_length=100, verbose_name="price"),
        ),
    ]
