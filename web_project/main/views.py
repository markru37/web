from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView   
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from .models import Human
from django.views.generic.base import View
from django.http import HttpResponseRedirect






def index(request):
    data ={
        'title':'Главная страница',

    }
    return render(request,'main/index.html', data )
    
def genres(request):
    data ={
        'title':'Жанры',
    }
    return render(request,'main/genres.html',data)
def games(request):
    data ={
        'title':'Информация',
    }
    return render(request,'main/games.html',data)



def registration(request):
    data ={
        'title':'Зарегистрироваться',
    }
    return render(request, 'main/registration.html',data)





class RegistrationFormView(TemplateView):
    template_name = 'registration.html'


def get(self, request):
    if request.user.is_authenticated:
        humans = Human.objects.all()
        ctx = {}
        ctx['humans'] = humans
        return render(request , self.template_name, ctx)
    else:
        return render(request, self.template_name, {})

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"

    success_url = "/"
    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutFormView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")

