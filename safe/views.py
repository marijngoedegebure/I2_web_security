from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, DeleteView
from message_module.models import Message
from safe.forms import SafeMessageForm


class CreateUserView(CreateView):
    template_name = 'safe/create_user_template.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save(commit=False)
        if len(User.objects.all()) < 1:
            user.is_staff = True
        user.save()
        return redirect('safe_home')

class CreateSafeMessageView(CreateView):
    template_name = 'safe/home.html'
    form_class = SafeMessageForm

    def get_context_data(self, **kwargs):
        context = super(CreateSafeMessageView, self).get_context_data()
        context['messages'] = Message.objects.all()
        return context

    def form_valid(self, form):
        message = form.save(commit=False)
        message.user = User.objects.get(id=self.request.user.id)  # use your own profile here
        message.save()
        return redirect('safe_home')

def delete_message_safe(request, pk):
    message = Message.objects.get(pk=pk)
    message.delete()
    return redirect('safe_home')
