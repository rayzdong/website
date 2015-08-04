from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from webops.models import RegisterForm


def home(request):
    return render_to_response('home.html')


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            return HttpResponseRedirect('success.html')
    else:
        user_form = RegisterForm()
        return render_to_response('register.html', {'user_form': user_form})
