from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from datetime import date
from django.views.generic import *
from app1.forms import EditProfileForm


import datetime
my_date = datetime.date.today() 
p_year, p_week, day_of_week = my_date.isocalendar()

#print("Week #" + str(p_week) + " of year " + str(p_year))
firstdayofweek = datetime.datetime.strptime(f'{p_year}-W{int(p_week)}-1', "%Y-W%W-%w").date()
lastdayofweek = firstdayofweek + datetime.timedelta(days=6.9)
#print(firstdayofweek)
#print(lastdayofweek)



def home(request):
	return render(request,'app1/home.html')





# Create your views here.
@login_required(login_url='/users/login/')
def createtodo(request):
	if request.method == 'GET':
		return render(request,'app1/createtodo.html')
	else:
		user=(request.session.get('userId'))
		date=(request.POST.get('cdate'))
		title=(request.POST.get('title'))
		discription=request.POST.get('disc')
		todo=ToDo(date=date,title=title,discription=discription,user=User(id=user))
		todo.save()
		return redirect('/todolist/')

@login_required(login_url='/users/login/')
def todolist(request):
	uid=(request.session.get('userId'))
	t=ToDo.objects.filter(user_id=uid).order_by('date')
	return render(request,'app1/todolist.html',{"x":t})


@login_required(login_url='/users/login/')
def todaylist(request):
	uid=(request.session.get('userId'))
	t=ToDo.objects.filter(user_id=uid,date=datetime.date.today()).order_by('date')
	return render(request,'app1/today-task.html',{"x":t})



@login_required(login_url='/users/login/')
def weeklist(request):
	uid=(request.session.get('userId'))
	
	t=ToDo.objects.filter(user_id=uid,date__range=[firstdayofweek,lastdayofweek]).order_by('date')
	return render(request,'app1/week-task.html',{"x":t})






@login_required(login_url='/users/login/')
def changetodo(request,id,status):
	todo=ToDo.objects.get(pk=id)
	print(status)
	todo.done=status
	todo.save()
	return redirect('/todolist/')






@login_required(login_url='/users/login/')
def update_view(request):
	
	if request.method=='POST':
		
		fm=EditProfileForm(request.POST,instance=request.user)
		if fm.is_valid():
			fm.save()
			return redirect('/view_profile/')
	else:
		
		fm=EditProfileForm(instance=request.user)
		return render(request,'app1/mydetails.html',{'form':fm})



@login_required(login_url='/users/login/')
def view_profile(request):
	uid=(request.session.get('userId'))
	u=User.objects.get(id=uid)
	return render(request,'app1/myprofile.html',{"i":u})