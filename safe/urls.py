from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView
from safe.views import CreateUserView, CreateSafeMessageView, delete_message_safe

urlpatterns = patterns('',
    url(r'^$', CreateSafeMessageView.as_view(), name='safe_home'),
    url(r'^delete/(?P<pk>\d+)$', delete_message_safe, name='safe_delete'),
    url(r'^create/$', CreateUserView.as_view(), name='safe_create'),
    url(r'^login/$', login, name='safe_login'),
    url(r'^login_success/$', TemplateView.as_view(template_name="safe/login_success.html"), name='safe_login_success'),
    url(r'^logout/$', logout, {'next_page':'/safe/logout_success/'}, name='safe_logout'),
    url(r'^logout_success/$', TemplateView.as_view(template_name="safe/logout_success.html"), name='safe_logout_success'),
)
