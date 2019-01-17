from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Category, TodoList
from .forms import CategoryForm, TodoForm


def index(request):
    form = TodoForm(request.POST or None)
    categories = Category.objects.all()
    if request.method == 'POST':
        if "taskAdd" in request.POST:
            try:
                form = TodoForm(request.POST or None)
                form.save()
                return redirect("todo:index")
            except Category.DoesNotExist:
                messages.error(request, "Please fill all")
                return redirect("todo:index")

    return render(request, 'todo/index.html', {'form': form, 'categories': categories})


def create(request):
    form = CategoryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('todo:index')

    return render(request, 'todo/create.html', {'form': form})


def edit(request, pk):
    context = {}
    try:
        data = TodoList.objects.get(id=pk)
    except TodoList.DoesNotExist:
        messages.error(request, 'Task not found')
        return redirect('todo:list')

    form = TodoForm(instance=data)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('todo:list')

    context['form'] = form
    return render(request, 'todo/create.html', context)


def list(request):
    context = {}
    data = TodoList.objects.all()
    context['data'] = data
    return render(request, 'todo/list.html', context)


def delete(request, pk):
    try:
        data = TodoList.objects.get(id=pk)
    except TodoList.DoesNotExist:
        messages.error(request, 'Task not found')
        return redirect('todo:list')
    data.delete()
    messages.success(request, 'Deleted Successfully')
    return redirect('todo:list')



