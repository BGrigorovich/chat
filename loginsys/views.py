from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from core.models import Messages


def login_view(request):
    args = {}
    args.update(csrf(request))
    args['messages'] = Messages.objects.all()
    args['login_form'] = AuthenticationForm()
    if request.POST:
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])
            login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Invalid user or password. Try again'
            return render_to_response('main.html', args, context_instance=RequestContext(request))
    else:
        return render_to_response('login.html', args, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    args = {}
    args.update(csrf(request))
    args['signup_form'] = UserCreationForm()
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = authenticate(username=new_user_form.cleaned_data['username'],
                                    password=new_user_form.cleaned_data['password2'])
            if not new_user.is_anonymous():
                login(request, new_user)
            return redirect('/')
        else:
            args['signup_form'] = new_user_form
    return render_to_response('signup.html', args, context_instance=RequestContext(request))
