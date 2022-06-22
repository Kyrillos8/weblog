from sre_constants import SUCCESS
from django.shortcuts import  render, redirect
from django.contrib.auth.models import User
from .forms import NewUserForm
from django.contrib.auth import login as Login_auth
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			Login_auth(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/account/profile")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="account/register.html", context={"register_form":form})



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/account/profile")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="account/login.html", context={"login_form":form})


def profile(request):
    return render(request, "account/profile.html")

def logout_user(request):
	logout(request)
	messages.success(request, "logged out successfuly")
	return redirect('/')    
