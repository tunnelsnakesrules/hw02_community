# yatube/urls.py
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('group_list/', include('posts.urls', namespace='posts')),
    path('', include('posts.urls', namespace='posts'))
]
