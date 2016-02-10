import json

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.template.context_processors import csrf
from rest_framework.generics import ListAPIView
from core.models import Messages
import logging
from .serializers import MessagesSerializer

logger = logging.getLogger('chat')


# todo: rename
def main_page(request):
    args = {}
    args.update(csrf(request))
    if request.is_ajax():
        request_body = json.loads(request.body.decode())
        message = request_body['message']
        logger.info('%s: %s', request.user, message)
        new_message = Messages(user=request.user, message=message)
        new_message.save()
        return
    else:
        args['form'] = AuthenticationForm()
        messages = Messages.objects.all()
        args['messages'] = messages
        return render_to_response('main.html', args, context_instance=RequestContext(request))


class MessagesView(ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
