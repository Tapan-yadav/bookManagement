from django.db import models

# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to="files")


class Book(models.Model):
    title = models.CharField(("title"), max_length=255)
    author = models.CharField(("author"), max_length=255)
    authors = models.CharField(("authors"), max_length=255)
    isbn13 = models.CharField(("isbn13"), max_length=150)
    isbn10 = models.CharField(("isbn10"), max_length=150)
    price = models.CharField(("price"), max_length=100)
    publisher = models.CharField(("publisher"), max_length=150)
    pubyear = models.IntegerField(("pubyear"))
    subjects = models.CharField(("subjects"), max_length=255)
    pages = models.CharField(("pages"), max_length=100, null=True)
