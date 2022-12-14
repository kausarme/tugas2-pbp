from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, toggle_task, create_task, delete_task, \
    add_task

from todolist.views import show_todolist_json, show_todolist_lama

app_name = "todolist"

urlpatterns = [
    path("", show_todolist, name="show_todolist"),
    path("lama", show_todolist_lama, name="show_todolist_lama"),
    path("register/", register, name="register"),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add/', add_task, name='add_task'),
    path("create-task/", create_task, name="create_task"),
    path("toggle-task/<int:id>", toggle_task, name="toggle_task"),
    path("delete-task/<int:id>", delete_task, name="delete_task"),
    path('json/', show_todolist_json, name='show_todolist_json'),
]
