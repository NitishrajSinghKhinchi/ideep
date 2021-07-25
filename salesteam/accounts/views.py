from django import forms
from django.shortcuts import render,redirect
from .forms import CustomerRegistrationForm, LoginForm,Workingform,Clientform
from .models import CustomUser,Working,Client
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
class CustomerregistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'accounts/customerregistration.html',{'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Registered Successfully')
            form.save()
            form=CustomerRegistrationForm()
        return render(request,'accounts/customerregistration.html',{'form':form})

# Login View Function
def user_login(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
      fm = LoginForm(request=request, data=request.POST)
      if fm.is_valid():
        uname = fm.cleaned_data['username']
        print(uname)
        upass = fm.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        if user is not None:
          login(request, user)
          messages.success(request, 'Logged in successfully !!')
          return redirect('/profile/')
    else: 
      fm = LoginForm()
    return render(request, 'accounts/login.html', {'form':fm})
  else:
    return redirect('/profile/')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        fm = Workingform(request.POST)
        if fm.is_valid():
            area = fm.cleaned_data['area_visited']
            person = fm.cleaned_data['total_person']
            leads = fm.cleaned_data['number_of_leads']
            print(area)
            print(person)
            reg = Working(area_visited=area,total_person=person,number_of_leads=leads)
            reg.save()
            return redirect('addclient')
    else:
        fm = Workingform()
    stud = Working.objects.all()
    return render(request, 'accounts/profile.html', {'form':fm, 'stu':stud})
 
@login_required
def add_client(request):
    if request.method == 'POST':
        fm = Clientform(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Clientform()
    else:
        fm = Clientform()
    stud = Client.objects.all()
    return render(request, 'accounts/clientdetails.html', {'form':fm, 'stu':stud})

@login_required
def update_data(request, id):
    if request.method == 'POST':
        pi = Client.objects.get(pk=id)
        fm = Clientform(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Details Updated !!!")
            return redirect('addclient')
    else:
        pi = Client.objects.get(pk=id)
        fm = Clientform(instance=pi)
    return render(request, 'accounts/update.html', {'form':fm})

@login_required
def delete_client(request, id):
    if request.method == 'POST':
        pi = Client.objects.get(pk=id)
        pi.delete()
        return redirect('addclient')