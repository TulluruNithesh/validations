from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.forms import *

def stud(request):
    form=StudentForm()
    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse('validate successfully')
    return render(request,'stud.html',context={'form':form})
