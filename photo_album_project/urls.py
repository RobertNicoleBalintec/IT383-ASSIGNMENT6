import sys
print("DEBUG: urls.py loading", file=sys.stderr)

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Test OK")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'gallery/signup.html', {'form': form})

urlpatterns = [
    path('test/', test_view, name='test'),
    path('admin/', admin.site.urls),
    path('', include('gallery.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='gallery/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
]

print("DEBUG: urls.py loaded successfully", file=sys.stderr)