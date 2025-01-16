from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class PagesViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        # Define static views to include in the sitemap
        return ['home-page', 'contacts-page', 'about-us-page']

    def location(self, item):
        # Return the URL for static views
        return reverse(item)
