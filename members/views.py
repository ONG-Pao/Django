
# from django.shortcuts import render
# from django.http import HttpResponse

# def members(request):
#     return HttpResponse("Hello Djano project")

# from django.http import HttpResponse
# from django.template import loader

# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())

# Displady Data............................................

from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(resquest):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
             'mymembers': mymembers,
             }
  return HttpResponse(template.render(context, resquest))

def details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template("main.html")
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request)) 

def evern(request):
  template = loader.get_template('template.html')
  context = {
    'Cars': ['Ford', 'Toyota', 'Zusuki'],   
  }
  return HttpResponse(template.render(context, request)) 

# def testing(request):
#   mydata = Member.objects.all()
#   template = loader.get_template('template.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))
