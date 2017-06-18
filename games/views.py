from django.views import generic
from .models import PaczkaGier
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth import logout



class IndexView(generic.ListView):
    template_name = 'games/index.html'
    context_object_name = 'all_games'
    def  get_queryset(self):
        return PaczkaGier.objects.all()


class DetailView(generic.DetailView):
    model=PaczkaGier
    context_object_name = 'paczka'
    template_name = 'games/detail.html'


class PaczkaCreate(CreateView):
    model= PaczkaGier
    fields = [ 'kreator_paczki', 'nazwa_paczki' , 'rodzaj_gier' , 'logo_paczki']

class PaczkaUpdate(UpdateView):
    model= PaczkaGier
    fields = [ 'kreator_paczki', 'nazwa_paczki' , 'rodzaj_gier' , 'logo_paczki']

class PaczkaDelete(DeleteView):
    model=PaczkaGier
    success_url = reverse_lazy('games:index')

class UserFormView(View):
    form_class = UserForm
    template_name='games/registration_form.html'

    def get(self,request):
        form =self.form_class(None)
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form =self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('games:index')
        return render(request,self.template_name, {'form':form})

def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/games/loggedin')
    else:
        return HttpResponseRedirect('games/invalid')

def loggedin(request):
    return render_to_response('loggedin.html',{'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')



