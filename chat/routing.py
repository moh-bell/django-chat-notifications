# chat/routing.py
from os import name
from channels import consumer
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/echo/$',consumers.EchoConsumer.as_asgi()),
    re_path(r"notifications/$", consumers.NotificationConsumer.as_asgi()),    # Url path for connecting to the websocket to send notifications.

]
