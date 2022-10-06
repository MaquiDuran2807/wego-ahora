from django.urls import path, include
from .views import LoginView, LogoutView , SignupView


urlpatterns = [
    # Auth views
    #login
    path('auth/login/',
        LoginView.as_view(), name='auth_login'),
    #logout
    path('auth/logout/',
        LogoutView.as_view(), name='auth_logout'),
    #registrar usuario
    path ('auth/signup/',SignupView.as_view(),name='auth_signup'),
    
    #recuperar contraseñas
    path ('auth/reset/',include('django_rest_passwordreset.urls',namespace='password_reset')),
]

from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # Aquí deberíamos mandar un correo al cliente...
    print(
        f"\nRecupera la contraseña del correo '{reset_password_token.user.email}' usando el token '{reset_password_token.key}' desde la API http://localhost:8000/api/auth/reset/confirm/")