# from rest_framework import status, generics
# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.views import APIView
from api.serializers import ReviewSerializer
from books.models import Review
from rest_framework import viewsets


class ReviewsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().order_by('-created_at')
    lookup_field = 'id'


# class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):  # APIView
#     permission_classes = [IsAuthenticated]
#     serializer_class = ReviewSerializer
#     queryset = Review.objects.all()
#     lookup_field = 'id'
#
#     # def get(self, request, id):
#     #     book_review = Review.objects.get(id=id)
#     #     serializer = ReviewSerializer(book_review)
#     #
#     #     return Response(data=serializer.data)
#     #
#     # def delete(self, request, id):
#     #     book_review = Review.objects.get(id=id)
#     #     book_review.delete()
#     #
#     #     return Response(status=status.HTTP_204_NO_CONTENT)
#     #
#     # def put(self, request, id):
#     #     book_review = Review.objects.get(id=id)
#     #     serializer = ReviewSerializer(instance=book_review, data=request.data)
#     #
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     #
#     #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     #
#     # def patch(self, request, id):
#     #     book_review = Review.objects.get(id=id)
#     #     serializer = ReviewSerializer(instance=book_review, data=request.data, partial=True)
#     #
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     #
#     #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ReviewsAPIView(generics.ListCreateAPIView):  # APIView
#     permission_classes = [IsAuthenticated]
#     serializer_class = ReviewSerializer
#     queryset = Review.objects.all().order_by("-created_at")
#
#     # def get(self, request):
#     #     book_review = Review.objects.all().order_by("-created_at")
#     #
#     #     paginator = PageNumberPagination()
#     #     page_obj = paginator.paginate_queryset(book_review, request)
#     #     serializer = ReviewSerializer(page_obj, many=True)
#     #
#     #     return paginator.get_paginated_response(serializer.data)
#     #
#     # def post(self, request):
#     #     serializer = ReviewSerializer(data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#     #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
