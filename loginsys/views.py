from django.contrib.auth import authenticate, login, logout
# from django.contrib import auth
from django.contrib.auth.context_processors import auth
# from django.http import request
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from core.models import Messages


def login_view(request):
    args = {}
    args.update(csrf(request))
    args['messages'] = Messages.objects.all()
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'No such user'
            return render_to_response('main.html', args, context_instance=RequestContext(request))
    else:
        return render_to_response('main.html', args, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = authenticate(username=new_user_form.cleaned_data['username'],
                                    email=new_user_form.cleaned_data['email'],
                                    password=new_user_form.cleaned_data['password'])
            login(request, new_user)
            return HttpResponseRedirect('/')
            # return redirect('/')
