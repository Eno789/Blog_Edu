from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, logout_then_login
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import SignUpForm

login = LoginView.as_view(template_name = "accounts/login_form.html")


@login_required
def logout(request):
    messages.success(request, "Success!!")
    return logout_then_login(request)

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '회원가입을 환영합니다.')
            return redirect("accounts:login")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup_form.html",
                  {
                      "form" : form
                  })