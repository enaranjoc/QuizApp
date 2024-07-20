from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True  # Redirige al usuario a la página principal después de iniciar sesión

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirige al usuario a la página de inicio de sesión después de cerrar sesión


@login_required
def home(request):
    return render(request, 'home.html')
