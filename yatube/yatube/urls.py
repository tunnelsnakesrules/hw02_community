from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('group_list/', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='posts'))
]
