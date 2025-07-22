
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from tasks.sitemaps import TaskSitemap

sitemaps = {
    'task': TaskSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
