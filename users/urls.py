from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProfileView, ProfileUpdateView
from home.views import home_page


app_name = 'users'
urlpatterns = [
    path('home/', home_page, name='home-page'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update-profile/', ProfileUpdateView.as_view(), name='update-profile'),
]