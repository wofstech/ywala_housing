from django.http import HttpResponse 
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login 
from .forms import MyHouseEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . models import Myhouses
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def addlisting(request):    
    if request.method == 'POST': 
        form = MyHouseEditForm(request.POST, files=request.FILES, )
        if form.is_valid():    
            Houses = form.save(commit=False)
            Houses.author=request.user
            Houses.save()
            return redirect('addlisting')           
    else:        
        form = MyHouseEditForm()  
    
    return render(request, 'houses/addlisting.html', {'form':form })


@login_required
def listbyuser (request):
    house_list = Myhouses.objects.filter(author=request.user)
    return render(request, 'houses/ListingByUser.html', {'house_list':house_list})

class UserListView(LoginRequiredMixin,generic.ListView):
    model = Myhouses
    template_name ='houses/ListingByUser.html'
    
    
    def get_queryset(self):
        return Myhouses.objects.filter(author=self.request.user)

class alllisting(LoginRequiredMixin,generic.ListView):
    model = Myhouses
    template_name ='houses/alllisting.html'
    paginate_by = 2


@login_required
def listbyuserdetails(request, id):
    house_list1 = Myhouses.objects.get(id = id)

    context = {
        'house_list1':house_list1
    }

    return render(request, 'houses/ListingByUserDetails.html', context)



