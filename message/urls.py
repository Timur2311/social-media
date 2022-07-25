from django.urls import path

from message.views import ChatListApiView, MessageCreateApiView, MessageListApiView

urlpatterns = [
    path('', ChatListApiView.as_view()),
    path('messages/', MessageListApiView.as_view()),
    path('messages/create', MessageCreateApiView.as_view()),
]
