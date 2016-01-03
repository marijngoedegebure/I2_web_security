from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, DeleteView
from message_module.models import Message
from unsafe.forms import UnSafeMessageForm


class CreateUserView(CreateView):
    template_name = 'unsafe/create_user_template.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save(commit=False)
        if len(User.objects.all()) < 1:
            user.is_staff = True
        user.save()
        return redirect('unsafe_home')

class CreateUnSafeMessageView(CreateView):
    template_name = 'unsafe/home.html'
    form_class = UnSafeMessageForm

    def get_context_data(self, **kwargs):
        context = super(CreateUnSafeMessageView, self).get_context_data()
        context['messages'] = Message.objects.all()
        return context

    def form_valid(self, form):
        message = form.save(commit=False)
        message.user = User.objects.get(id=self.request.user.id)  # use your own profile here
        message.save()
        return redirect('unsafe_home')

def delete_message_unsafe(request, pk):
    message = Message.objects.get(pk=pk)
    message.delete()
    return redirect('unsafe_home')
