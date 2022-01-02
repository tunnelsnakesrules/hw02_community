"""
Комментарий добавлен для того чтобы исправить ошибку выдающую Pylint,
 я проверял на ошибки с Flake8
"""
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    posts = Post.objects.all()[:10]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    title = "Здесь будет информация о группах проекта Yatube"
    context = {
        'group': group,
        'title': title,
        'posts': posts,
        'text': 'Информация о группах',
    }
    return render(request, 'posts/group_list.html', context)
