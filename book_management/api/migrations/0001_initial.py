# Generated by Django 4.1.6 on 2023-03-19 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                ("author", models.CharField(max_length=255, verbose_name="author")),
                ("authors", models.CharField(max_length=255, verbose_name="authors")),
                ("isbn13", models.CharField(max_length=150, verbose_name="isbn13")),
                ("isbn10", models.CharField(max_length=150, verbose_name="isbn10")),
                ("price", models.FloatField(verbose_name="price")),
                (
                    "publisher",
                    models.CharField(max_length=150, verbose_name="publisher"),
                ),
                ("pubyear", models.IntegerField(verbose_name="pubyear")),
                ("subjects", models.CharField(max_length=255, verbose_name="subjects")),
                ("pages", models.IntegerField(verbose_name="pages")),
            ],
        ),
    ]
