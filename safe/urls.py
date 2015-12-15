from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from safe.views import CreateUserView

urlpatterns = patterns('',
    url(r'^create/$', CreateUserView.as_view(), name='create'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
)
