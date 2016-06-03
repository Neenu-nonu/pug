from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from registeration import views
from registeration.views import *
from registeration.models import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='registeration_user'),
]
