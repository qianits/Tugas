from django.urls import path
from todolist.views import show_todolist
from todolist.views import logout_user, login_user, register, create_task, remove, status

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('remove/<int:id>', remove, name='remove'),
    path('status/<int:id>', status, name='status'),
]