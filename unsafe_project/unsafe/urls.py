from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView
from .views import CreateUnSafeMessageView, delete_message_unsafe, CreateUnsafeUserView, csrf

urlpatterns = patterns('',
    url(r'^$', CreateUnSafeMessageView.as_view(), name='unsafe_home'),
    url(r'^delete/(?P<pk>\d+)$', delete_message_unsafe, name='unsafe_delete'),
    url(r'^create/$', CreateUnsafeUserView.as_view(), name='unsafe_create'),
    url(r'^login/$', login, name='unsafe_login'),
    url(r'^login_success/$', TemplateView.as_view(template_name="unsafe/login_success.html"), name='unsafe_login_success'),
    url(r'^logout/$', logout, {'next_page':'/unsafe/logout_success/'}, name='unsafe_logout'),
    url(r'^logout_success/$', TemplateView.as_view(template_name="unsafe/logout_success.html"), name='unsafe_logout_success'),
    url(r'^csrf/$', csrf, name='csrf'),
)
