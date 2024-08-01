from django.urls import path
from .views import detail, my_profile, EditBio, search_users, Register, DeleteProfile
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('<int:pk>/', detail, name='profile-detail'),
    path('<int:pk>/edit/bio/', EditBio.as_view(), name='edit_bio'),
    path('<int:pk>/delete/', DeleteProfile.as_view(), name='delete_user'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('my_profile', my_profile, name="my-profile"),
    path('search/', search_users, name='search'),
    path('register/', Register.as_view(), name='register'),
]

