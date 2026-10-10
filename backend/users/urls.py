from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('customers/', views.UserListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.UserDetailView.as_view(), name='customer-detail'),
]
