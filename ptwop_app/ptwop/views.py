from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import *


# Create your views here.
def frontpage(request):
    return render(request, 'ptwop/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            
            return redirect('frontpage')
    
    else:
        form = SignUpForm()

    return render(request, 'ptwop/signup.html', {'form' : form})