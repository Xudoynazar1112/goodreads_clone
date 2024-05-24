from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from books.forms import ReviewForm
from books.models import Book, Review


class BooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by("id")
        search_query = request.GET.get("q", '')
        if search_query:
            books = books.filter(title__icontains=search_query)
        page_size = request.GET.get('page_size', 2)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        return render(request, "books/list.html", {"page_obj": page_obj, "search_query": search_query})


class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        review_form = ReviewForm()
        return render(request, "books/book_detail.html", {"book": book, "review_form": review_form})


class AddReviewVeiw(LoginRequiredMixin, View):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            Review.objects.create(
                book=book,
                user=request.user,
                stars_given=review_form.cleaned_data["stars_given"],
                comment=review_form.cleaned_data["comment"]
            )

            return redirect(reverse("books:detail", kwargs={"id": book.id}))
        return render(request, "books/book_detail.html", {"book": book, "review_form": review_form})


class EditReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.review_set.get(id=review_id)
        review_form = ReviewForm(instance=review)
        content = {
            "book": book,
            "review": review,
            "review_form": review_form
        }

        return render(request, "books/edit_review.html", content)

    def post(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.review_set.get(id=review_id)
        review_form = ReviewForm(instance=review, data=request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect(reverse("books:detail", kwargs={"id": book.id}))

        content = {
            "book": book,
            "review": review,
            "review_form": review_form
        }

        return render(request, "books/edit_review.html", content)


class ConfirmDeleteView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.review_set.get(id=review_id)
        content = {
            "book": book,
            "review": review,
        }
        return render(request, "books/confirm_delete.html", content)


class DeleteView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.review_set.get(id=review_id)
        review.delete()
        messages.success(request, "You have successfully deleted the review!")
        return redirect(reverse("books:detail", kwargs={"id": book.id}))
