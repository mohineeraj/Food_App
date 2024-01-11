from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
	if request.method=='POST':
		first_name=request.POST['First_name']
		last_name=request.POST['last_name']
		Username=request.POST['Username']
		PASSWORD=request.POST['PASSWORD']
		Confirm_Password=request.POST['confirm_pass']
		email=request.POST['email']
		if PASSWORD==Confirm_Password:
			if User.objects.filter(username=Username).exists():
				messages.info(request,"User Taken")
				return redirect('/')
			elif User.objects.filter(email=email).exists():
				messages.info(request,"Email Taken")
			else:
				if Username[0].isalpha():
					if len(email)>6:
						pass
					else:
						messages.info(request,"Invalid Email entered")
						return redirect('/')

					user=User.objects.create_user(username=Username,first_name=first_name,last_name=last_name,password=PASSWORD,email=email)
					user.save();
					print("user created")
					return redirect('login')
				else:
					messages.info(request,"Username should be start with Alpabetics")
					return redirect('/')

		else:
			messages.info(request,"Password not matching")
			return redirect('/')
		return redirect('/')
		
	else:
		return render(request,'Welcome.html')
def login(request):
	if request.method=='POST':
		USERNAME=request.POST['uname']
		PASSWORD=request.POST['psw']
		user=auth.authenticate(username=USERNAME, password=PASSWORD)
		if user is not None:
			auth.login(request,user)	
			return redirect('Orders')
		else:
			messages.info(request,"Invalid details")
			return render(request,'Login.html')
	else:	
		return render(request,'Login.html')


def logout(request):
	auth.logout(request)
	return redirect('login')