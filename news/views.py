from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from .models import Post
from index.admin import Section


def render_news(request):
    post_list = get_list_or_404(Post)
    paginator = Paginator(post_list, 6)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    first_section = Section.objects.get(order=1)
    second_section = Section.objects.get(order=2)
    third_section = Section.objects.get(order=3)
    fourth_section = Section.objects.get(order=4)

    context = {
        'first_section': first_section,
        'second_section': second_section,
        'third_section': third_section,
        'fourth_section': fourth_section,
        'posts': posts
    }

    return render(request, 'news/news.html', context)


def render_new_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'news/new-detail.html', {'post': post})
