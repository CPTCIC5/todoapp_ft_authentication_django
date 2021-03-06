from django.urls import path
from . import views

app_name='app1'

urlpatterns = [
    path('',views.index,name='index'),
    path('add_todo/',views.add_todo,name='add_todo'),
    path('delete/<int:question_id>/',views.delete_todo,name='delete_todo'),
    path('edit/<str:text>/',views.edit_todo,name='edit_todo'),
    path('contact/',views.contact,name='contact'),
]