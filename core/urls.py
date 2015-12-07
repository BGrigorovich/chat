from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from .views import main_page, signup_page, MessagesView

urlpatterns = [
    url(r'^$', main_page),
    url(r'^main/signup$', signup_page),
    url(r'^signup$', signup_page),
    url(r'^main$', lambda request: redirect(reverse_lazy('main_page'))),
    url(r'^messages', MessagesView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
