# from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'api'
router = DefaultRouter()
router.register('reviews', ReviewsViewSet, basename='review')

urlpatterns = router.urls

# urlpatterns = [
#     path("reviews/", ReviewsAPIView.as_view(), name='review-list'),
#     path("reviews/<int:id>/", ReviewDetailAPIView.as_view(), name='review-detail'),
# ]
