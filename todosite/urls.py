from django.contrib import admin
from django.urls import path
from todo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name = 'todo'),
    path('del/<int:id>',remove,name = 'del')
]
