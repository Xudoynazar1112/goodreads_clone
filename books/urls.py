from django.urls import path
from books.views import *

app_name = "books"
urlpatterns = [
    path("", BooksView.as_view(), name='list'),
    path("<int:id>/", BookDetailView.as_view(), name="detail"),
    path("<int:id>/review/", AddReviewVeiw.as_view(), name="review"),
    path("<int:book_id>/reviews/<int:review_id>/edit/", EditReviewView.as_view(), name="edit-review"),
    path("<int:book_id>/reviews/<int:review_id>/delete/confirm/", ConfirmDeleteView.as_view(), name="delete-confirm"),
    path("<int:book_id>/reviews/<int:review_id>/delete/", DeleteView.as_view(), name="delete"),
]