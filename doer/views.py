from django.views.generic import ListView

from doer.models import Tag, Task
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic


class HomeView(ListView):
    model = Task
    template_name = "home.html"
    context_object_name = "tasks"


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("doer:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("doer:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("doer:task-list")


def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = True
    task.save()
    return redirect("doer:task-list")


def undo_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = False
    task.save()
    return redirect("doer:task-list")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "name"
    success_url = reverse_lazy("doer:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("doer:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("doer:tag-list")
