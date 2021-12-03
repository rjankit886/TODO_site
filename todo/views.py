from django.shortcuts import render,redirect
from django.contrib import messages
from todo.forms import *
from todo.models import *

# Create your views here.
def index(request):
	item_list = Todo.objects.order_by('-date')
	
	if request.method == 'POST':
		form = TodoForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect('todo')

	else:
		form = TodoForm()
		page = {'forms':form, 'list':item_list, 'title':'TODO List'}
	
	return render(request,'index.html',page)

def remove(request,id):
	item = Todo.objects.get(id = id)
	item.delete()
	messages.info(request,'item removed')
	return redirect('todo')