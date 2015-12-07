from django.conf.urls import include, url
from django.contrib import admin
from core import urls as core_urls
from loginsys import urls as loginsys_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += core_urls.urlpatterns
urlpatterns += loginsys_urls.urlpatterns
