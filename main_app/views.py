from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #automatically log in any newly created user
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid signup, try agian'
    #If we click signup, thats a GET req, so we hit this code
    #If we hit submit (that's POST) and the form isn't valid, we hit this code and show another empty form         
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)