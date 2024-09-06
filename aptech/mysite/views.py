from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.template import loader
from mysite.models import Contact
from django.views.decorators.csrf import csrf_protect, requires_csrf_token, ensure_csrf_cookie

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def aboutus(request):
    template = loader.get_template('aboutus.html')
    return HttpResponse(template.render())

def contactus(request):
    #template = loader.get_template('contactus.html')
    contact = Contact.objects.all().values()
    context = {"context": contact}
    return render(request,'contactus.html',context)

def details(request,id):
    #template = loader.get_template('contactus.html')
    contact = Contact.objects.get(id=id)
    context = {"context": contact}
    return render(request,'details.html',context)

def delete(request,id):
    contact = Contact.objects.get(id=id)   
    contact.delete()
    return redirect('contactus')

@csrf_protect
def savecontact(request):
    id = int(request.POST['id'])
    name = request.POST['name']
    email = request.POST['email']
    age = request.POST['age']
    contact = Contact(id, name, email,  age)
    contact.save()
    return redirect('contactus')

@csrf_protect
def updatecontact(request):
    id = int(request.POST['id'])
    name = request.POST['name']
    email = request.POST['email']
    age = request.POST['age']
    contact =Contact.objects.get(id=id)
    contact.name = name
    contact.email = email
    contact.age = age
    contact.save()
    return redirect('contactus')