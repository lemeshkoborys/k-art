from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from .models import Post


def render_news(request):
    post_list = get_list_or_404(Post)
    paginator = Paginator(post_list, 6)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'news/news.html', {'posts': posts})


def render_new_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'news/new-detail.html', {'post': post})
