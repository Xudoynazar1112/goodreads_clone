from django.test import TestCase
from django.urls import reverse

from books.models import Book, Review
from users.models import CustomUser


class HomePageTest(TestCase):
    def test_paginated_list(self):
        book = Book.objects.create(title="Book1", description="Description1", isbn="123456")
        user = CustomUser.objects.create(username='Abdulhay', first_name="Xudoynazar", last_name="Saparov",
                                         email="saparovxudoynazar@gamil.com")
        user.set_password("something")
        user.save()

        review1 = Review.objects.create(book=book, user=user, stars_given=3, comment="Very good book")
        review2 = Review.objects.create(book=book, user=user, stars_given=4, comment="Useful book")
        review3 = Review.objects.create(book=book, user=user, stars_given=5, comment="Amazing book")

        response = self.client.get(reverse("landing_page") + "?page_size=2")

        self.assertContains(response, review3.comment)
        self.assertContains(response, review2.comment)
        self.assertNotContains(response, review1.comment)
