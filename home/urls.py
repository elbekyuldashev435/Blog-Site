from django.urls import path
from .views import home_page, AboutView, AboutUpdateView


app_name = 'home'
urlpatterns = [
    path('', home_page, name='home-page'),
    path('about/', AboutView.as_view(), name='about'),
    path('about-update/', AboutUpdateView.as_view(), name='about-update')
]