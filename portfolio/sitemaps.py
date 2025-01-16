from django.contrib.sitemaps import Sitemap
from .models import Portfolio
from django.urls import reverse

class PortfolioSitemap(Sitemap):
    changefreq = 'weekly'  # Frequency of content updates
    priority = 0.8  # Priority for SEO purposes (1.0 is the highest)

    def items(self):
        return Portfolio.objects.all()

    def location(self, item):
        # Ensure the slug is passed here
        return reverse('detail_portfolio', kwargs={'slug': item.slug})
    
    def lastmod(self, obj):
        # Use the last modified timestamp for each entry
        return obj.date_create


class PortfolioViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        # Define static views to include in the sitemap
        return ['portfolio-page']

    def location(self, item):
        # Return the URL for static views
        return reverse(item)