
from django.shortcuts import render, redirect
from django.contrib import messages


from .models import Users,Mechanics, Workshops, Reviews,Call
from django.db.models import Q
from .forms import *


# Create your views here.
def Homefun(request):
    return render(request, "Home.html")

def UserLogoutfun(request):
    if request.method == "POST":
          return redirect('Home')

def MechanicLogoutfun(request):
    if request.method == "POST":
          return redirect('Home')


def UserSignupfun(request):
    if request.method == "POST":
        if request.POST.get('username') and request.POST.get('pass1') and request.POST.get(
                'pass2'):
            users1 = Users()

            users1.username = request.POST.get('username')
            users1.pass1 = request.POST.get('pass1')
            users1.pass2 = request.POST.get('pass2')
            

        

        if Users.objects.filter(username= users1.username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('UserSignup')

        if len(users1.username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('UserSignup')

        if users1.pass1 != users1.pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('UserSignup')

        if not (users1.username).isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('UserSignup')

        if users1.username and users1.pass1 and users1.pass2 :
            users1.save()
            messages.success(request,
                             "Your Account has been created succesfully!! ")
        return render(request, 'UserSignin.html')
    else:
        return render(request, 'UserSignup.html')


def UserSigninfun(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        users1 = Users.objects.get(username=username, pass1=pass1)
        if users1:

            username = users1.username
            pass1 = users1.pass1
            request.session['username'] = username
            request.session['pass1'] = pass1
            return redirect('USER')
        else:
            messages.error(request, "Invalid Credentials!!")
            return redirect('UserSignin')

    return render(request, 'UserSignin.html')


def MechanicSigninfun(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        mechanics = Mechanics.objects.get(username=username, pass1=pass1)
        if mechanics:

            username = mechanics.username
            pass1 = mechanics.pass1
            request.session['username'] = username
            request.session['pass1'] = pass1

            return redirect('approval')
        else:

            messages.error(request, "Invalid Credentials!!")

            return redirect('MechanicSignin')
    return render(request, 'MechanicSignin.html')


def MechanicSignupfun(request):
    if request.method == "POST":
        if request.POST.get('username') and request.POST.get('pass1') and request.POST.get(
                'pass2') :
            mechanics1 = Mechanics()

            mechanics1.username = request.POST.get('username')
            mechanics1.pass1 = request.POST.get('pass1')
            mechanics1.pass2 = request.POST.get('pass2')
           

            

            if Mechanics.objects.filter(username=mechanics1.username):
                messages.error(request, "Username already exist! Please try some other username.")
                return redirect('MechanicSignup')

            if len(mechanics1.username) > 20:
                messages.error(request, "Username must be under 20 charcters!!")
                return redirect('MechanicSignup')

            if mechanics1.pass1 != mechanics1.pass2:
                messages.error(request, "Passwords didn't matched!!")
                return redirect('MechanicSignup')

            if not mechanics1.username.isalnum():
                messages.error(request, "Username must be Alpha-Numeric!!")
                return redirect('MechanicSignup')

            if mechanics1.username and mechanics1.pass1 and mechanics1.pass2 :
                mechanics1.save()
                messages.success(request,
                                 "Your Account has been created succesfully!! ")
            return render(request, 'MechanicSignin.html')
    else:
        return render(request, 'MechanicSignup.html')


def USERfun(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(address__icontains=q) | Q(shop_name__icontains=q))
        Workshop = Workshops.objects.filter(multiple_q)
        context = {
            'Workshop': Workshop
        }
        return render(request, 'shops.html', context)
    else:
        Workshop = Workshops.objects.all()
        context = {
            'Workshop': Workshop
        }
        return render(request, 'shops.html', context)


def reviewfun(request):
    form = ReviewsForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['Enter_Name']
        review = form.cleaned_data['Write_review']

        s = Reviews(Enter_Name=name, Write_review=review)
        s.save()
    return render(request, 'review.html', {'form': form})

def callfun(request):
    form = CallForm(request.POST or None)
    if form.is_valid():
        Mobile_no = form.cleaned_data['Mobile_no']
        SMS = form.cleaned_data['SMS']

        d = Call(Mobile_no=Mobile_no, SMS=SMS)
        d.save()
    return render(request, 'call.html', {'form': form})



def reviewstatusfun(request):
    title = "Reviews"
    queryset = Reviews.objects.all()

    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, 'reviewstatus.html', context)

def callstatusfun(request):
    title = "Call"
    queryset = Call.objects.all()

    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, 'callstatus.html', context)

def approvalfun(request):
    title = "Request"
    queryset = Request.objects.all()

    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, 'approval.html', context)




def applyrequestfun(request):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['Enter_Name']
        Vehicle_type = form.cleaned_data['Vehicle_type']
        Vehicle_no = form.cleaned_data['Vehicle_no']
        Problem = form.cleaned_data['Problem']
        s = Request(Name=name, Vehicle_type=Vehicle_type,Vehicle_no=Vehicle_no,Problem=Problem)
        s.save()

    return render(request, 'applyrequest.html',{form :'form'})


def user_request_view(request):

    title = "Request"
    queryset = Request.objects.all()

    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request,"status.html",context)

def user_approve_request(request,k_id):
    g=Request.objects.get(id=k_id)
    g.status=1
    g.save()
    return redirect("approval")

def user_disapprove_request(request,k_id):
    k=Request.objects.get(id=k_id)
    k.status=2
    k.save()
    return redirect("approval")




