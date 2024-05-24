from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Review


def landing_page(request):
    all_reviews = Review.objects.all().order_by('-created_at')
    page_size = request.GET.get('page_size', 4)
    paginator = Paginator(all_reviews, page_size)

    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'landing.html', {"page_obj": page_obj})
