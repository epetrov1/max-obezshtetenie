from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home-page"),
    path("contacts/", views.contacts_page, name="contacts-page"),
    path("about-us/", views.about_us_page, name="about-us-page"),
]