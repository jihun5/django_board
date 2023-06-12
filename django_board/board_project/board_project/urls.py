from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls), 
    # admin으로 들어오는 url 빼고는 아래 path로 redirect 
    # path('', ), url 넣을 공간
]
