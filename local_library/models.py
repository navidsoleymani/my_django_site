from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField()
    birthday = models.DateField()
    degree = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "نویسنده‌ها"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    summary = models.TextField()
    GENRE_SELECTED = [
        ('a', 'A_type'),
        ('b', 'B_type'),
        ('d', 'D_type'),
        ('e', 'E_type')
    ]
    genre = models.CharField(choices=GENRE_SELECTED, max_length=1)

    class Meta:
        verbose_name_plural = "کتاب‌ها"
