from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    degree = models.IntegerField(default=0)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)