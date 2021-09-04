from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.

#Signup View

def signup(request):
	if request.method=='POST':
		fm=UserForm(request.POST)
		
		if fm.is_valid():
			fm.save()
			return redirect('/users/login/')
	else:
		fm=UserForm()
	return render(request,'users/signup.html',{'form':fm})


#Login View

def user_login(request):
	if request.method=='POST':
		fm=AuthenticationForm(request=request,data=request.POST)
		if fm.is_valid():
			uname=fm.cleaned_data['username']
			upass=fm.cleaned_data['password']
			user=authenticate(username=uname,password=upass)
			if user is not None:
				
				request.session['userId']=user.id
				request.session['userName']=uname
				login(request,user)

				# if user.username=='admin':
				# 	return redirect('/users/home/')
				

				if 'next' in request.POST:
					return redirect(request.POST.get('next'))
				else:	
					return redirect('/users/home/')
	else:			
		fm=AuthenticationForm()
	return render(request,'users/login.html',{'form':fm})

@login_required(login_url='/users/login/')
def user_logout(request):
	logout(request)
	return redirect('/users/login/')


@login_required(login_url='/users/login/')
def home(request):
	return render(request,'users/home.html')



