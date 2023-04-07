from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def django_form(request):
    FO=Studentform()
    d={'form':FO}
    if request.method=='POST':
        FD=Studentform(request.POST)
        if FD.is_valid():
            n=FD.cleaned_data['name']
            a=FD.cleaned_data['age']
            e=FD.cleaned_data['email']
            ad=FD.cleaned_data['address']
            g=FD.cleaned_data['gender']
            D={'n':n,'a':a,'e':e,'ad':ad,'g':g}
            return render(request,'form_data.html',D)
    return render(request,'django_form.html',d)

