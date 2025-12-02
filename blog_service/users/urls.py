from django.urls import path
from .views import RegisterView, LoginView, UserDetailView, VerifyTokenView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('verify-token/', VerifyTokenView.as_view(), name='verify-token'),


]