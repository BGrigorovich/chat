from django.conf.urls import url
from .views import main_page, MessagesView

urlpatterns = [
    url(r'^$', main_page, name='home'),
    url(r'^messages', MessagesView.as_view(), name='messages'),
]