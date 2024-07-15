from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    # <> is to put a params
    path("<int:id>", views.book_detail, name="book-detail")
]
