from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import TaskPagination

# Add these imports to your existing views.py
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy


class TaskListCreateView(generics.ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
    pagination_class = TaskPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["is_completed", "priority"]
    search_fields = ["title"]


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]


# Add these class-based views for templates
class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"
    paginate_by = 9

    def get_queryset(self):
        queryset = Task.objects.all()

        # Search functionality
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(title__icontains=search)

        # Filter by priority
        priority = self.request.GET.get("priority")
        if priority:
            queryset = queryset.filter(priority=priority)

        # Filter by completion status - FIXED LOGIC
        is_completed = self.request.GET.get("is_completed")
        if is_completed is not None and is_completed != "":
            # Convert string to boolean properly
            if is_completed.lower() == "true":
                queryset = queryset.filter(is_completed=True)
            elif is_completed.lower() == "false":
                queryset = queryset.filter(is_completed=False)

        return queryset


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"


class TaskCreateView(CreateView):
    model = Task
    template_name = "tasks/task_form.html"
    fields = ["title", "description", "priority", "due_date", "is_completed"]
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        messages.success(self.request, "Task created successfully!")
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "tasks/task_form.html"
    fields = ["title", "description", "priority", "due_date", "is_completed"]
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        messages.success(self.request, "Task updated successfully!")
        return super().form_valid(form)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("task-list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Task deleted successfully!")
        return super().delete(request, *args, **kwargs)
