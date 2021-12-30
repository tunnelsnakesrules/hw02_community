# posts/views.py
from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    posts = Post.objects.order_by('-pub_date')[:10]
    title = "Здесь будет информация о группах проекта Yatube"
    group = get_object_or_404(Group, slug=slug)
    context = {
        'group': group,
        'title': title,
        'posts': posts,
        'text': 'Информация о группах'
    }
    return render(request, 'posts/group_list.html', context)
