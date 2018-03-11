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

@login_required
def addlisting(request):    
    if request.method == 'POST': 
        form = MyHouseEditForm(request.POST, files=request.FILES)
        if form.is_valid():           
            Houses = form.save(commit=False)
            Houses.save()
            return redirect('ListingByUser')           
    else:        
        form = MyHouseEditForm()  

    return render(request, 'houses/addlisting.html', {'form':form })

class ListingByUser(LoginRequiredMixin, generic.ListView):  
    model = Myhouses
    template_name ='houses/ListingByUser.html'
    paginate_by = 10
    def get_queryset(self):
        return Myhouses.objects.filter(author=self.request.user)

