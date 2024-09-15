from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

urlpatterns = [
        path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name= 'logout'),
]

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            form = CustomUserCreationForm()
        return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'blog/profile.html')
