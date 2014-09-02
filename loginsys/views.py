# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from  django.contrib import auth
from  django.contrib.auth.forms import UserCreationForm
from  django.core.context_processors import csrf

#авторизация
#зашита csrf
# обработка пост запросов
# ошибки авторизации

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            args['login_error'] = 'Пользователь не найден'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html',args)

# выходы из пользователя
def logout(request):
    auth.logout(request)
    return redirect('/')

# регистрация пользователя
# защита csrf
# обрабодка постзапросов
#вход в систему
# работа с формой регистрации
def register(request):
    args={}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username = new_user_form.cleaned_data['username'], password = new_user_form.cleaned_data['password2'])
            auth.login(request, new_user)
            return redirect('/')
        else:
            args['form'] = new_user_form
    return render_to_response('register.html', args)