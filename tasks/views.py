from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Todo


def index(request):
  if request.method == 'POST':
    task = request.POST['task']
    if task:
      Todo.objects.create(task=task, pub_date=timezone.now())
    return HttpResponseRedirect('/')
  else:
    todos = Todo.objects.all()
    return render(request, "index.html", {'todos': todos })

def detail(request, id):
  if request.method == 'POST':
    Todo.objects.get(id=id).delete()
  
  return HttpResponseRedirect("/")
  
