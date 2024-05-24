from django.contrib.auth import get_user
from users.models import CustomUser
from django.test import TestCase
from django.urls import reverse


class RegistrationTestCase(TestCase):
    def test_user_is_created(self):
        self.client.post(
            reverse('users:register'),
            data={
                'username': "Xudoynazar",
                "first_name": "Xudoynazar",
                "last_name": "Saparov",
                "email": "saparovxudoynazar@gmail.com",
                "password": "alloh1112"
            }
        )
        user = CustomUser.objects.get(username="Xudoynazar")
        self.assertEqual(user.first_name, "Xudoynazar")
        self.assertEqual(user.last_name, "Saparov")
        self.assertEqual(user.email, "saparovxudoynazar@gmail.com")
        self.assertNotEqual(user.password, "alloh1112")
        self.assertTrue(user.check_password("alloh1112"))

    def test_required_fields(self):
        response = self.client.post(
            reverse('users:register'),
            data={
                'username': "Xudoynazar",
                "email": "saparovxudoynazar@gmail.com"
            }
        )
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 0)

        self.assertFormError(response, "form", "username", "This field is required.")
        self.assertFormError(response, "form", "email", "This field is required.")

    def test_invalid_email(self):
        response = self.client.post(
            reverse('users:register'),
            data={
                'username': "Xudoynazar",
                "first_name": "Xudoynazar",
                "last_name": "Saparov",
                "email": "invalid-email",
                "password": "alloh1112"
            }
        )
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "email", "Enter a valid email address.")

    def test_unique_username(self):
        user = CustomUser.objects.create(username='xudoynazar', first_name="Xudoynazar")
        user.set_password("password")
        user.save()

        response = self.client.post(
            reverse('users:register'),
            data={
                'username': "Xudoynazar",
                "first_name": "Xudoynazar",
                "last_name": "Saparov",
                "email": "invalid-email",
                "password": "alloh1112"
            }
        )

        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 1)

        self.assertFormError(response, "form", "username", "A user with that username already exist.")


class LoginTestCase(TestCase):
    def setUp(self):
        self.db_user = CustomUser.objects.create(username='xudoynazar', first_name="Xudoynazar", last_name="Saparov",
                                           email="saparovxudoynazar@gmail.com")
        self.db_user.set_password("something")
        self.db_user.save()

    def test_successful_login(self):
        self.client.post(
            reverse("users:login"),
            data={
                "username": "xudoynazar",
                "password": "something"
            }
        )

        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_wrong_credential(self):
        self.client.post(
            reverse("users:login"),
            data={
                "username": "wrong-username",
                "password": "something"
            }
        )
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

        self.client.post(
            reverse("users:login"),
            data={
                "username": "xudoynazar",
                "password": "wrong_password"
            }
        )
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_logout(self):
        self.client.login(username="xudoynazar", password="something")
        self.client.get(reverse("users:logout"))

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)


class ProfileTestCase(TestCase):
    def test_login_Required(self):
        response = self.client.get(reverse("users:profile"))
        self.assertEqual(response.url, reverse("users:login") + "?next=/users/profile/")

    def test_profile_detail(self):
        user = CustomUser.objects.create(username='Abdulhay', first_name="Xudoynazar", last_name="Saparov",
                                   email="saparovxudoynazar@gamil.com")
        user.set_password("something")
        user.save()

        self.client.login(username="Abdulhay", password="something")
        response = self.client.get(reverse("users:profile"))
        self.assertContains(response, user.username)
        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)

    def test_profile_edit(self):
        user = CustomUser.objects.create(username='Abdulhay', first_name="Xudoynazar", last_name="Saparov",
                                   email="saparovxudoynazar@gamil.com")
        user.set_password("something")
        user.save()

        self.client.login(username="Abdulhay", password="something")
        response = self.client.post(
            reverse("users:profile_edit"),
            data={
                "username": "Abdulhay",
                "first_name": "Po'lat",
                "last_name": "Saparov",
                "email": "saparovxudoynazar@gamil.com"
            }
        )
        user = CustomUser.objects.get(pk=user.pk)
        # user.refresh_from_db()
        self.assertEqual(user.first_name, "Po'lat")
        self.assertEqual(response.url, reverse("users:profile"))
