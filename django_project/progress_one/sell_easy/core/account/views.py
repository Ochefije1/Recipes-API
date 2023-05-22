from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from .models import Profile
from core.models import Store

# Create your views here.

def login(request):
    if request.method == 'POST':
        form =LoginForm(request.POST)
        try:
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                
                user = authenticate(email=email, password=password)
                
                
            if user is not None:
                request.session['user_id'] = str(user.id)
                return redirect('dashboard')
                   
            
        except ValidationError as err:
            return render(request, 'account/login.html', {'form':form, 'error': err})
            
    form = LoginForm()
    return render(request, 'account/login.html', {'form':form})
                  
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            username = form.cleaned_data['email']
            username = form.cleaned_data['first_name']
            username = form.cleaned_data['last_name']
            username = form.cleaned_data['aaddress']
            username = form.cleaned_data['phone_number']
            user = profile(username=username, email=email, first_ )
            form.save()
            return redirect('login')
    form = SignUpForm()
    return render(request, 'account/signup.html', {'form':form})
               

    
def dashboard(request):
    user_id = request.session['user_id']
    user = Profile.objects.get(id=user_id)
    store = Store.objects.get(owner=user)
    return render(request, 'account/dashboard.html', {'user':user})



