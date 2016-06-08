from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from registeration import views
from registeration.views import *
from registeration.models import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='registeration_user'),
    url(r'user/success/', TemplateView.as_view(template_name='success.html'),
     name='page'),
    url(r'^chocolate/add/', AddChocolateView.as_view(), name="add_c"),
    url( r'^chocolate/info/(?P<choco_id>\d+)/$', ChocolateDetailsView.as_view(), name="chocolate_info")
]



#url(r'^user/success/', TemplateView.as_view(template_name='register_user1.html'),
    #name='eg'),