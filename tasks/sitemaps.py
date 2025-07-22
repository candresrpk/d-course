from django.contrib.sitemaps import Sitemap
from .models import Task


class TaskSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Task.objects.all()

    def lastmod(self, obj):
        return obj.updated_at