from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pages/', include('pages.urls', namespace='pages')),
    path('', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls)
]
