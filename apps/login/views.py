from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count 
from models import User

def session_check(request):
    if 'user' in request.session:
        return True
    else:
        return False

def index(request):
    if session_check(request):
        return redirect('donate:index')
        # ^^ REDIRECT TO APP ^^
    
    context = {
        'top_donors': User.objects.filter(user_type=0).order_by('-donations')[:5]
    }

    return render(request,'login/index.html', context)

def login_reg(request):
    if request.POST['action'] == 'register':
        result = User.objects.validate_reg(request)

    elif request.POST['action'] == 'login':
        result = User.objects.validate_login(request)

    if result[0] == False:
        print_errors(request, result[1])
        return redirect('login:index')

    return log_user_in(request, result[1])

def print_errors(request, error_list):
    for error in error_list:
        messages.add_message(request, messages.INFO, error)

def log_user_in(request, user):
    request.session['user'] = {
        'user_id': user.id,
        'user_type': user.user_type,
        'name': user.name
    }
    return redirect('donate:index')
    # ^^ REDIRECT TO APP ^^

def logout(request):
    request.session.clear()

    return redirect('login:index')

def success(request):
    return render(request, 'login/success.html', context)

def donate_hack(request):
    user = User.objects.get(id=request.session['user']['user_id'])
    user.donations += 1
    user.save()
    return redirect('donate:index')
