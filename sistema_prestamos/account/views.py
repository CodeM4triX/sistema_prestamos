from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.contrib import messages

@never_cache
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

@never_cache
def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                messages.success(request, "Has iniciado sesión correctamente.")
                return redirect("home")  # Cambia esto a la vista que quieras redirigir después del login
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

@never_cache
def user_logout(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect("login")
