from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Category, TodoList
from .forms import CategoryForm, TodoForm


def index(request):
    todos = TodoForm(request.POST or None)
    to = TodoList.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        if "taskAdd" in request.POST:
            try:
                todos = TodoForm(request.POST or None)
                # title = request.POST["description"]
                # category = request.POST["category_select"]
                # content = title + " -- " + " -- " + category
                # Todo = TodoList(title=title, content=content, category=Category.objects.get(name=category))
                todos.save()
                return redirect("todo:index")
            except Category.DoesNotExist:
                messages.error(request, "Please fill all")
                return redirect("todo:index")

        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))
                todo.delete()

    return render(request, "todo/index.html", {"todos": todos, 'categories': categories, 'to': to})


def create(request):
    form = CategoryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('todo:index')

    return render(request, 'todo/create.html', {'form': form})



