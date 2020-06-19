from django.http import HttpResponse
from django.shortcuts import render
from . import models


def index(request):
    num_authors = models.Author.objects.all().count()
    num_books = models.Book.objects.all().count()
    return render(
        request,
        'local_library/index.html', context={'num_authors': num_authors, 'num_books': num_books},
    )
