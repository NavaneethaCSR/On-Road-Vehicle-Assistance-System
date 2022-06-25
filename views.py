from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.conf import settings
from.models import Users,Mechanics
from django.contrib.auth.forms import AuthenticationForm

def Homefun(request):
    return render(request,'Home.html')



def UserSigninfun(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, pass1=pass1,pass2=pass2)

        if user is not None:
            login(request, user)

            # messages.success(request, "Logged In Successfully!!")
            return render(request, "USER.html")
        else:
            messages.error(request,(" There was an error logging in,Try again"))
            return redirect('UserSignin')
    else:
            return render(request, "UserSignin.html")



def MechanicSigninfun(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                pass1 = form.cleaned_data.get('pass1')
                user = authenticate(username=username, password=pass1)
                if user is not None:
                    login(request, user)
                    return redirect('MechanicSignin')
                else:
                    messages.error(request, "Invalid username or password")
            else:
                messages.error(request, "Invalid username or password")
        return render(request, 'MechanicSignin.html',
                      context={'form': AuthenticationForm()})



def MechanicSignupfun(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('MechanicSignup')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters!!")
            return redirect('MechanicSignup')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('MechanicSignup')

        if len(pass1) < 8:
            messages.error(request, "Password should be atleast 8 characters!!")
            return redirect('MechanicSignup')

        if not pass1.capitalize():
            messages.error(request, "Password must have one  Uppercase and Lower case  character!!")
            return redirect('MechanicSignup')
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('MechanicSignup')
        if not pass1.isalnum():
            messages.error(request, "Password must be Alpha-Numeric!!")
            return redirect('MechanicSignup')

        if username and pass1:
            user = Mechanics(username=username,password=pass1)

            user.save()
            return redirect('MechanicSignin')
        else:

            return redirect('MechanicSignin')
    return render(request, "MechanicSignup.html")





def UserSignupfun(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('UserSignup')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters!!")
            return redirect('UserSignup')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('UserSignup')

        if len(pass1) < 8:
            messages.error(request, "Password should be atleast 8 characters!!")
            return redirect('UserSignup')

        if not pass1.capitalize():
            messages.error(request, "Password must have one  Uppercase and Lower case  character!!")
            return redirect('UserSignup')
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('UserSignup')
        if not pass1.isalnum():
            messages.error(request, "Password must be Alpha-Numeric!!")
            return redirect('UserSignup')

        if username and pass1 and pass2:
            user1 = User(username=username,pass1=pass1,pass2=pass2)
            user1.save()
            return redirect('UserSignin')

        else:

            return redirect('UserSignin')

    return render(request, "UserSignup.html")

