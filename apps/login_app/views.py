from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def root(request) :
    if 'first_name' not in request.session :
        request.session['first_name'] = ""
    if 'last_name' not in request.session :
        request.session['last_name'] = ""
    if 'email' not in request.session :
        request.session['email'] = ""
    if 'username' not in request.session :
        request.session['username'] = ""
    if 'password' not in request.session :
        request.session['password'] = ""
    if 'confirm' not in request.session :
        request.session['confirm'] = ""
    if 'check' not in request.session :
        request.session['check'] = "no"
    return render(request, 'login_app/root.html')

def login(request) :
    errors = User.objects.login(request.POST, request.session)
    if len(errors) > 0 :
        for key, value in errors.items() :
            messages.error(request,value, extra_tags='login')
        return redirect('/')
    else :
        return redirect('/budget')

def register(request) :
    errors = {}
    error = User.objects.fname_validator(request.POST)
    if len(error) > 0:
        errors.update(error)
    error = User.objects.lname_validator(request.POST)
    if len(error) > 0:
        errors.update(error)
    error = User.objects.username_validator(request.POST)
    if len(error) > 0:
        errors.update(error)
    error = User.objects.email_validator(request.POST)
    if len(error) > 0:
        errors.update(error)
    error = User.objects.password_validator(request.POST)
    if len(error) > 0:
        errors.update(error)
    error = User.objects.confirm_validator(request.POST)
    if len(error) > 0:
        errors.update(error)
    if len(errors) > 0:
        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['email'] = request.POST['email']
        request.session['username'] = request.POST['username']
        request.session['password'] = request.POST['password']
        request.session['confirm'] = request.POST['confirm']
        request.session['login_check'] = "yes"
        messages.error(request,"Please fix errors", extra_tags='register')
        return redirect('/')
    else :
        del request.session['first_name']
        del request.session['last_name']
        del request.session['email']
        del request.session['username']
        del request.session['password']
        del request.session['confirm']
        if 'login_check' in request.session:
            del request.session['login_check']
        request.session['userid'] = User.objects.add_User(request.POST)
        return redirect('/budget')

@csrf_exempt
def firstname(request) :
    if request.method == 'POST':
        errors = User.objects.fname_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items() :
                messages.error(request,value, extra_tags='firstname')
    return render(request, 'login_app/partials/firstname.html')

@csrf_exempt
def lastname(request) :
    if request.method == 'POST':
        errors = User.objects.lname_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items() :
                messages.error(request,value, extra_tags='lastname')
    return render(request, 'login_app/partials/lastname.html')

@csrf_exempt
def username(request) :
    if request.method == 'POST':
        errors = User.objects.username_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items() :
                messages.error(request,value, extra_tags='username')
    return render(request, 'login_app/partials/username.html')

@csrf_exempt
def email(request) :
    if request.method == 'POST':
        errors = User.objects.email_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items() :
                messages.error(request,value, extra_tags='email')
    return render(request, 'login_app/partials/email.html')

@csrf_exempt
def password(request) :
    if request.method == 'POST':
        errors = User.objects.password_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items() :
                messages.error(request,value, extra_tags='password')
    return render(request, 'login_app/partials/password.html')

@csrf_exempt
def confirm(request) :
    if request.method == 'POST':
        errors = User.objects.confirm_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items() :
                messages.error(request,value, extra_tags='confirm')
    return render(request, 'login_app/partials/confirm.html')

def logout(request) :
    if 'userid' in request.session:
        del request.session['userid']
    return redirect('/')