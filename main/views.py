from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.views import View
# Create your views here.
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.shortcuts import resolve_url
from django.views import View
from django.shortcuts import redirect

from .bulkng import Bulkng

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

# Create your views here.


@login_required(login_url="/accounts/login")
def gethome(request: HttpRequest) -> HttpResponse:
    print(request.user)
    template_name = 'home.html'
    return render(request, template_name)

@login_required(login_url="/accounts/login")
def posthome(request: HttpRequest) -> HttpResponse:
    sf = request.POST['sent_from']
    to = request.POST['to']
    body = request.POST['body']
    instance = Bulkng()
    instance.send(sf,to,body)
    messages.success(request, 'sent')
    return redirect('/home')
    
@login_required(login_url="/accounts/login")
def postlogout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('/home')