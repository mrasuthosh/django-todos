from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.forms import TodoForm
from todoapp.models import Todo
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView , DeleteView

# Create your views here.



class Tasklistview(ListView):
    model = Todo
    template_name = 'index.html'
    context_object_name = 'task1'

class Taskdetailview(DetailView):
    model = Todo
    template_name = 'details.html'
    context_object_name = 'task'

class Taskupdateview(UpdateView):
    model = Todo
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','proirety','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('Tasklistview')

def todo(request):
    task1=Todo.objects.all()
    if request.method=='POST':
        nm=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Todo(name=nm,proirety=priority,date=date)
        task.save()
    return render(request,'index.html',{'task1':task1})

# def details(request):
#
#     return render(request,'details.html',)

def delete(request,taskid):
    task=Todo.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    task=Todo.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'f':f})
