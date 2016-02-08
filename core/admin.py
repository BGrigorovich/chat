from django.contrib import admin
from core.models import Messages, MessagesAdmin

admin.site.register(Messages, MessagesAdmin)
