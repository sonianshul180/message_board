# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.message_board, name='message_board'),
    path('delete/<int:msg_id>/', views.delete_message, name='delete_message'),
]
