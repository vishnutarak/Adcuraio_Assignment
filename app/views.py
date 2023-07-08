from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ViewSet
from app.serializers import *
from rest_framework.response import Response
from django.views.generic import CreateView,TemplateView

def home(request):
    
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    

    return render(request,'home.html')

def registration(request):
    ufo=UserForm()
    d={'ufo':ufo}

    if request.method=='POST':
        ufd=UserForm(request.POST)
        if ufd.is_valid():
            NSUO=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()
            return HttpResponse('Regsitration is Susssessfulll')
        else:
            return HttpResponse('Not valid')

    return render(request,'registration.html',d)




def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid username or password') 
        
    return render(request,'login_user.html')

class hello(TemplateView):
    template_name = 'hello.html'

@login_required
def logout_user(request):
    return HttpResponseRedirect(reverse('hello'))


@login_required
def conform_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_user'))
    

class ActorsData(ViewSet):
    def list(self,request):
        ADO=Actors.objects.all()
        SJD=ActorSerializer(ADO,many=True)
        d={'data':SJD.data}
        return render(request,'list.html',d)
    
    def retrieve(self,request,pk):
        TO=Actors.objects.get(pk=pk)
        SDO=ActorSerializer(TO)
        return Response(SDO.data)

    def update(self,request,pk):
        SPO=Actors.objects.get(pk=pk)
        SPD=ActorSerializer(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'data is updated'})
        else:
            return Response({'Failed':'Data is Not Updated'})
    
    def partial_update(self,request,pk):
        SPO=Actors.objects.get(pk=pk)
        SPD=ActorSerializer(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'data is updated'})
        else:
            return Response({'Failed':'data is Not Updated'})
    def destroy(self,request,pk):
        Actors.objects.get(pk=pk).delete()
        return Response({'Deleted':'data is deleted'})
    

    