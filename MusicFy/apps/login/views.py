from django.shortcuts import render, redirect

from django.contrib import messages
from models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def registration_page(request):
    return render(request, "login/registration.html")

def registration(request):
    errors = User.objects.validate_user(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/')
    
    else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

            User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed_pw)
            user = User.objects.get(email=email)
            request.session['id'] = user.id
            messages.success(request, 'Successfully Registered')
            id = request.session['id']
            return redirect('/music/{}'.format(id))

def login_page(request):
    return render(request, 'login/login.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.filter(email=email)

    if len(user) < 1:
        messages.error(request, "User does not exists")
        return redirect('/')
    
    else:
        cpassword = bcrypt.checkpw(password.encode(), user[0].password.encode())
        if cpassword:
            request.session['id'] = user[0].id
            messages.success(request, 'Successfully Logged In')
            id = request.session['id']
            return redirect('/music/{}'.format(id))
        else:
            messages.error(request, "Incorrect username/password combination.")
            return redirect('/')

def loggedin(request):
    return redirect("/music/")

def logout(request):
    request.session.clear()
    return redirect('/')