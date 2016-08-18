from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from .models import User

# Create your views here.
def index(request):
    return render(request,'login/index.html')


def login(request):
    user=User.objects.login(request.POST)
    try:
        request.session['user'] = {'name':user.name,
        'email':user.email}
        return redirect(reverse('success'))
    except:
        # no name or email, so do errory stuff here
        # add a flash message here!
        return redirect(reverse('index'))

def register(request):
    user=User.objects.register(request.POST)
    try:
        request.session['user'] = {'name':user.name,
        'email':user.email}
        return redirect(reverse('success'))
    except:
        # no name or email, so do errory stuff here
        # add a flash message here!
        return redirect(reverse('index'))



def success(request):
    return render(request,'login/success.html')
