from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data["username"]
            messages.success(request, f"Account created for {user_name}")
            return redirect("blog-home")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})
