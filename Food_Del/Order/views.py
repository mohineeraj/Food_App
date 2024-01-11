from django.shortcuts import render, redirect
from .models import FoodMenu, Ord_ADD
from .forms import ADDForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def Orders(request):
	dish=FoodMenu.objects.all()	
	return render(request,'Order1.html', {'dishes':dish})

def PlaceOrd(request):
	if request.method == 'POST':
		form=ADDForm(request.POST)
		if form.is_valid():
			if request.user.is_authenticated:
				form.save()
				Category=Ord_ADD.objects.all()
				#return redirect('cart')
				return render(request,'Ordered.html')
			#return redirect('cart')
	else:
		form=ADDForm()
		Category=Ord_ADD.objects.all()
		return render(request,'PlaceORD.html',{'Category':Category, 'form':form})

def cart(request):
	return render(request,'Ordered.html')
