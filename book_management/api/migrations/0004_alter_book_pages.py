# Generated by Django 4.1.6 on 2023-03-19 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_book_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="pages",
            field=models.IntegerField(null=True, verbose_name="pages"),
        ),
    ]
