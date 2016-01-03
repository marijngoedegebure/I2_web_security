from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect, render_to_response, render

# Create your views here.
from django.template import RequestContext
from django.views.generic import CreateView, DeleteView, FormView
from message_module.models import Message
from unsafe.forms import UnSafeMessageForm, UnSafeUserForm
from unsafe.models import UnsafeUser


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

class CreateUnsafeUserView(CreateView):
    template_name = 'unsafe/create_user_template.html'
    form_class = UnSafeUserForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        user = form.save(commit=False)
        if len(UnsafeUser.objects.all()) < 1:
            user.is_admin = True
        user.save()
        return redirect('unsafe_home')

class LoginFormView(FormView):
    template_name = 'unsafe/login.html'
    form_class = UnSafeUserForm

    def form_valid(self, form):
        unsafe_user = form.save(commit=False)
        if UnsafeUser.objects.get(username=unsafe_user.username, password=unsafe_user.password):
            return render(self.request, 'unsafe/login_success.html', context={"unsafe_user": unsafe_user})
        else:
            return redirect('unsafe_login')
