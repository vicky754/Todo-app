from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [


    path('',home),
    path('create-todo/',createtodo),
    path('todolist/',todolist),
    path('change-status/<int:id>/<str:status>/',changetodo),
    path('todaylist/',todaylist),
    path('UpdateUser/',update_view),
    path('view_profile/',view_profile),
    path('weeklist/',weeklist),

    
]




