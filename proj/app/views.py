from django.shortcuts import render, get_object_or_404
from app.models import Profile, Event
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required 
def newsfeed(request):
    if (request.GET.get('q', '') == ''):
        profiles = Profile.objects.filter(active=True)
    else:
        profiles = Profile.objects.filter(interests__icontains=request.GET.get('q', ''))
    return render(request, 'app/newsfeed.html', {'profiles': profiles})
 
@login_required 
def profile(request, slug):
    # get the Post object
    profile = get_object_or_404(Profile, slug=slug)
    # now return the rendered template
    return render(request, 'app/profile.html', {'profile': profile})

def index(request):
    return render(request, 'app/index.html', {})

def aboutus(request):
    return render(request, 'app/aboutus.html', {})

def loginview(request):
    return render(request, 'app/loginview.html', {})    

@login_required
def home(request):
    events = Event.objects.all()
    return render(request, 'app/home.html', {'events': events})    

@login_required
def edit(request):
    return render(request, 'app/edit.html', {}) 

def register(request):
    return render(request, 'app/register.html', {})

def deauthorize(request):
    logout(request)
    return HttpResponseRedirect('../')			


def authorize(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
			login(request, user)
			return HttpResponseRedirect('../home')			
        else:
            print('account disabled, sorry!')
    else:
        print('oops, wrong login')
        return HttpResponseRedirect('../')			

