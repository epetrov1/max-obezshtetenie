from django.shortcuts import render
from django.views.generic import ListView
from portfolio.models import Portfolio

# Create your views here.

class HomePageView(ListView):
    model = Portfolio
    template_name = 'pages/index.html'  # Make sure the template name matches your setup
    ordering = ['-date_create']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Portfolio.objects.values_list('tag', flat=True).distinct()
        return context


def contacts_page(request):
    return render(request, 'pages/contacts_page.html')


def about_us_page(request):
    return render(request, 'pages/about_us_page.html')


def custom_404(request, exception):
    return render(request, 'pages/404.html', status=404)
