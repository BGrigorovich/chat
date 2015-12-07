import json
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.template.context_processors import csrf
from rest_framework.generics import ListAPIView
from core.models import Messages
import logging
from .serializers import MessagesSerializer

logger = logging.getLogger('chat')


def signup_page(request):
    return render_to_response('signup.html', {}, context_instance=RequestContext(request))


def main_page(request):
    args = {}
    args.update(csrf(request))
    if request.is_ajax():
        print('ajax')
        request_body = json.loads(request.body.decode())
        message = request_body['message']
        logger.info('%s: %s', request.user, message)
        Messages.save(Messages.create(user=request.user, message=message))
        return
    else:
        print('not ajax')
        messages = Messages.objects.all()
        return render_to_response('main.html', {'messages': messages}, context_instance=RequestContext(request))


class MessagesView(ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
