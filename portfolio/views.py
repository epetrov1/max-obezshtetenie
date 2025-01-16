from django.views.generic import ListView, DetailView

from .models import Portfolio

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'  # Make sure this matches your template location
    context_object_name = 'portfolio'

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)
        # Get the current portfolio object
        current_portfolio = self.object
        # Retrieve all portfolio objects with the same tag as the current portfolio
        related_portfolios = Portfolio.objects.filter(tag=current_portfolio.tag).exclude(id=current_portfolio.id)
        # Add the related portfolios to the context
        context['related_portfolios'] = related_portfolios
        return context

class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio_list.html'  # Make sure the template name matches your setup
    ordering = ['-date_create']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Portfolio.objects.values_list('tag', flat=True).distinct()
        return context
    


