from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.template.context_processors import csrf
from core.models import Messages
import logging


logger = logging.getLogger('chat')


def main_page(request):
    messages = Messages.objects.all()
    return render_to_response('main.html', {'messages': messages}, context_instance=RequestContext(request))


def signup_page(request):
    return render_to_response('signup.html', {}, context_instance=RequestContext(request))


@login_required
def send_message(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        message = request.POST.get('message', '')
        logger.info(str(request.user) + ': ' + message)
        Messages.save(Messages.create(user=request.user, message=message))
        return redirect('/')
