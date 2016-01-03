from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect, render_to_response, render

# Create your views here.
from django.template import RequestContext
from django.views.generic import CreateView, DeleteView, FormView
from message_module.models import Message
from unsafe.forms import UnSafeMessageForm, UnsafeUserCreateForm
from unsafe.models import UnsafeUser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

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

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CreateView, self).dispatch(request, *args, **kwargs)

def delete_message_unsafe(request, pk):
    message = Message.objects.get(pk=pk)
    message.delete()
    return redirect('unsafe_home')

class CreateUnsafeUserView(FormView):
    template_name = 'unsafe/create_user_template.html'
    form_class = UnsafeUserCreateForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        cleaned_data = form.data
        user = User.objects.create_user(cleaned_data['username'], '', '')

        if len(UnsafeUser.objects.all()) < 1:
            user.is_staff = True
        if 'is_staff' in cleaned_data.keys():
            if cleaned_data['is_staff'] == 'on':
                user.is_staff = True
        user.save()
        unsafe_user = UnsafeUser.objects.create(user=user, plaintext_password=cleaned_data['plaintext_password'])
        unsafe_user.save()
        return redirect('unsafe_home')

def csrf(request):
    return render(request, 'unsafe/csrf.html');
