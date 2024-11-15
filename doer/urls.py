from django.urls import path
from doer import views
from doer.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("tags/", views.TagListView.as_view(), name="tag_list"),
    path("tags/add/", views.TagCreateView.as_view(), name="tag-add"),
    path("tags/update/<int:pk>/", views.TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", views.TagDeleteView.as_view(), name="tag-delete"),
    path("tasks/", views.TaskListView.as_view(), name="task-list"),
    path("tasks/add/", views.TaskCreateView.as_view(), name="add_task"),
    path("tasks/update/<int:pk>/", views.TaskUpdateView.as_view(), name="update_task"),
    path("tasks/delete/<int:pk>/", views.TaskDeleteView.as_view(), name="delete_task"),
    path("tasks/complete/<int:pk>/", views.complete_task, name="complete_task"),
    path("tasks/undo/<int:pk>/", views.undo_task, name="undo_task"),
]

app_name = "doer"
