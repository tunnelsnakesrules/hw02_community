"""
Комментарий добавлен для того чтобы исправить ошибку выдающую Pylint,
 я проверял на ошибки с Flake8
"""
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group, User
from django.contrib.auth.decorators import login_required
from .forms import PostForm


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


def profile(request, username):
    template = 'posts/profile.html'
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = Post.objects.filter(author=user).count()
    context = {
        'page_obj': page_obj,
        'author': user,
        'count': count,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    text = post.text
    text_title = text[:30]
    pub_date = post.pub_date
    author = post.author
    name = author.get_full_name()
    count_posts = author.posts.all().count()
    group = post.group
    context = {
        'text': text,
        'pub_date': pub_date,
        'name': name,
        'count_posts': count_posts,
        'author': author,
        'group': group,
        'text_title': text_title,

    }
    return render(request, template, context)


@login_required
def post_create(request):
    template = 'posts/create_post.html'
    select_group = Group.objects.all()
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.instance.author = request.user
        form.save()
        return redirect('posts:profile', username=request.user.username)
    context = {
        'form': form,
        'select_group': select_group,
    }
    return render(request, template, context)