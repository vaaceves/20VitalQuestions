from django.shortcuts import render
from .models import Topic, Question
from .forms import LoginUserForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView, ListView, TemplateView, FormView
from django import template


# Create your views here.
#
# SPANISH VIEWS
#
# index
def index_spa(request):
    topic1 = Topic.objects.get(id=1)
    topic2 = Topic.objects.get(id=2)
    topic3 = Topic.objects.get(id=3)
    topic4 = Topic.objects.get(id=4)
    topic5 = Topic.objects.get(id=5)

    context_dic = {
        'topic1': topic1,
        'topic2': topic2,
        'topic3': topic3,
        'topic4': topic4,
        'topic5': topic5,
    }

    return render(request, 'questions/spa/index.html', context_dic)


# login
class LoginUserViewSpa(View):
    login_form = LoginUserForm()
    login_error_message = None
    template = 'questions/spa/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('index_spa')
        return render(request, self.template, self.get_context())

    def post(self, request, *args, **kwargs):
        username_post = request.POST['username']
        password_post = request.POST['password']
        user = authenticate(username=username_post, password=password_post)
        if user is not None:
            login_django(request, user)
            return redirect('index_spa')
        else:
            self.login_error_message = "Username or Password invalid"
        return render(request, self.template, self.get_context())

    def get_context(self):
        return {
            'login_form': self.login_form,
            'login_error_message': self.login_error_message
        }


#
# ENGLISH VIEWS
#
# index
def index_eng(request):
    topic1 = Topic.objects.get(id=1)
    topic2 = Topic.objects.get(id=2)
    topic3 = Topic.objects.get(id=3)
    topic4 = Topic.objects.get(id=4)
    topic5 = Topic.objects.get(id=5)

    context_dic = {
        'topic1': topic1,
        'topic2': topic2,
        'topic3': topic3,
        'topic4': topic4,
        'topic5': topic5,
    }

    return render(request, 'questions/eng/index.html', context_dic)


# login
class LoginUserViewEng(View):
    login_form = LoginUserForm()
    login_error_message = None
    template = 'questions/eng/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('index_eng')
        return render(request, self.template, self.get_context())

    def post(self, request, *args, **kwargs):
        username_post = request.POST['username']
        password_post = request.POST['password']
        user = authenticate(username=username_post, password=password_post)
        if user is not None:
            login_django(request, user)
            return redirect('index_eng')
        else:
            self.login_error_message = "Username or Password invalid"
        return render(request, self.template, self.get_context())

    def get_context(self):
        return {
            'login_form': self.login_form,
            'login_error_message': self.login_error_message
        }


#
# LOGOUT
#
@login_required(login_url='home')
def logout(request):
    logout_django(request)
    return redirect('index_eng')


register = template.Library()


@register.filter
def to_en(value):
    return value.replace("es", "en")


@register.filter
def to_spa(value):
    return value.replace("en", "es")
