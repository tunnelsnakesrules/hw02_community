from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('auth/', include('users.urls', namespace='users')),
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
    path('group_list/', include('posts.urls', namespace='posts')),
    path('auth/', include('django.contrib.auth.urls')),
]
