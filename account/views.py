from django.http import HttpResponse 
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login 
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, HouseEditForm, TrialForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User



def user_login(request):    
    if request.method == 'POST':        
        form = LoginForm(request.POST)        
        if form.is_valid():            
            cd = form.cleaned_data            
            user = authenticate(username=cd['username'],                                
            password=cd['password'])            
            if user is not None:                
                if user.is_active:                    
                    login(request, user)                    
                    return HttpResponse('Authenticated '\
                'successfully')                
                else:                    
                        return HttpResponse('Disabled account')
            else:                
                        return HttpResponse('Invalid login')    
    else:        
        form = LoginForm()    
        return render(request, 'account/login.html', {'form': form}) 


@login_required 
def dashboard(request):
    profile = Profile.objects.all() 
    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'profile': profile}) 

def register(request):    
    if request.method == 'POST':        
        user_form = UserRegistrationForm(request.POST)        
        if user_form.is_valid():            
            # Create a new user object but avoid saving it yet            
            new_user = user_form.save(commit=False)            
            # # Set the chosen password                             
            new_user.set_password(                
            user_form.cleaned_data['password'])            
            # Save the User object            
            new_user.save() 
            profile = Profile.objects.create(user=new_user)            
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:        
         user_form = UserRegistrationForm()    
         return render(request, 'account/register.html', {'user_form': user_form}) 

@login_required 
def edit(request):    
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST) 
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():            
            user_form.save()            
            profile_form.save()
            messages.success(request, 'Profile updated successfully') 
        else:            
             messages.error(request, 'Error updating your profile') 
    
    else:        
        user_form = UserEditForm(instance=request.user)        
        profile_form = ProfileEditForm(instance=request.user.profile) 

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def addhouses(request):    
    if request.method == 'POST': 
        form = HouseEditForm(request.POST, files=request.FILES)
        if form.is_valid():           
            Houses = form.save(commit=False)
            Houses.save()
            return redirect('addhouses')           
    else:        
        form = HouseEditForm()  

    return render(request, 'account/addhouses.html', {'form':form }) 

def test(request):
    if request.method == "POST":
        form = TrialForm(request.POST)
        if form.is_valid():
            trial = form.save(commit=False)
            trial.save()
            return redirect('test')
    else:
        form = TrialForm()
    return render(request, 'account/trial.html', {'form': form})
