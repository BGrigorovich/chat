from django.conf.urls import url
from .views import login_view, logout_view, signup_view

urlpatterns = [
    url(r'^login/$', 'loginsys.views.login_view', name='login'),
    url(r'^logout/$', 'loginsys.views.logout_view', name='logout'),
    url(r'^signup_from/$', 'loginsys.views.signup_view', name='signup_form'),
    # url(r'^login/$', login_view),
    # url(r'^logout/$', logout_view),
    # url(r'^signup_from/$', signup_view),
]