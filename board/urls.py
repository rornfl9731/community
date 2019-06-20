from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from registration.views import *
from board.views import board_list,board_detail,board_write,boardUpdateView,board_delete,comment_delete

urlpatterns = [
    path('list/',board_list,name='list'),
    path('detail/<int:pk>', board_detail,name='detail'),
    path('write/',board_write,name='write'),
    path('update/<int:pk>/',boardUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',board_delete,name='delete'),
    path('delete/comment/<int:pk>',comment_delete,name='comment_delete'),


]