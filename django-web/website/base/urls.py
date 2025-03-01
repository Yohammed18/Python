from .views import PendingList, TaskDetail, CreateTask, EditTask, DeleteTask, Login, RegisterPage
from django.contrib.auth.views import LogoutView
from django.urls import path


urlpatterns = [
    path('', PendingList.as_view(), name='tasks'),
    path('login/', Login.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('edit-task/<int:pk>', EditTask.as_view(), name='edit-task'),
    path('delete-task/<int:pk>', DeleteTask.as_view(), name='delete-task'),
    
]