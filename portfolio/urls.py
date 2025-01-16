from django.urls import path
from . import views

urlpatterns = [
    path("", views.PortfolioListView.as_view(), name="portfolio-page"),
    path('portfolio/<slug:slug>/', views.PortfolioDetailView.as_view(), name='detail_portfolio'),
]