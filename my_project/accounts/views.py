from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy,reverse
from django.views import generic
from django.contrib.auth.models import User
from .models import CustomUser
from .forms import UpdateForm
# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def UserInfo(request,username):
    use = User.objects.get(username = username)
    if request.method == "POST":
        form = UpdateForm(request.POST)
        try:
            user = use.customuser
            user.delete()
        except(CustomUser.DoesNotExist):
            pass 
        customuser = form.save(commit=False)
        customuser.user = use
        customuser.save()
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'home.html', context={'user' : use,})

def ViewProfile(request, username):
    user = User.objects.get(username = username)
    return render(request, 'profile.html', context ={'user': user} )

def UpdateProfile(request, username):
    form = UpdateForm()
    user = User.objects.get(username=username)
    return render(request, 'update.html', {'form': form, 'username': username})

