from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    # template = loader.get_template('home.html')
    context={
        'name':"Aptech",
        'course':"Django"
    }
    return render(request,'home.html',context)