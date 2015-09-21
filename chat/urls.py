from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from core import views
from loginsys import views
from django.shortcuts import redirect
import core
import loginsys

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/', core.views.main_page),
    url(r'^main/signup/$', core.views.signup_page),
    url(r'^signup/$', core.views.signup_page),
    url(r'^$', lambda request: redirect(reverse_lazy('core.views.main_page'))),
    url(r'^login/$', 'loginsys.views.login_view', name='login'),
    url(r'^logout/$', 'loginsys.views.logout_view', name='logout'),
    url(r'^signup_from/$', 'loginsys.views.signup_view', name='signup_form'),
    url(r'^send_message/$', 'core.views.send_message', name='send_message'),
]
