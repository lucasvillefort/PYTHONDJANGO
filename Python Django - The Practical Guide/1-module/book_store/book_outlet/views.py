from ast import Try
from django.http import Http404
from django.shortcuts import render
from .models import Book

# Create your views here.


def index(request):
    # Book.objects.filter()
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})


def book_detail(request, id):
    try:
        book = Book.objects.get(pk=id)  # primary key
        return render(
            request,
            "book_detail.html",
            {
                "title": book.title,
                "author": book.author,
                "rating": book.rating,
                "is_bestseller": book.is_bestselling,
            },
        )
    except:
        raise Http404()
