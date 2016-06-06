from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView, UpdateView
from registeration.forms import *# Create your views here.
from registeration import settings
from django.shortcuts import redirect


class Home(TemplateView):
   template_name="index.html"

class UserRegistrationView(AnonymousRequiredMixin, FormView):
   template_name = "register_user.html"
   authenticated_redirect_url = reverse_lazy(u"home")
   form_class = UserRegistrationForm
   success_url = '/registeration/user/success/'

   def form_valid(self, form):
       form.save()
       return FormView.form_valid(self, form)

def anonymous_required(func):
    def as_view(request, *args, **kwargs):
        redirect_to = kwargs.get('next', settings.LOGIN_REDIRECT_URL )
        if request.user.is_authenticated():
            return redirect(redirect_to)
        response = func(request, *args, **kwargs)
        return response
    return as_view

class AddChocolateView(FormView):
    template_name = "add_chocolate.html"
    form_class = ChocolateAddForm
    success_url = '/registeration/chocolate/success'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)
