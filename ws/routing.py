from django.urls import re_path

from .consumers import EchoConsumer, GroupEchoConsumer

websocket_urlpatterns = [
    re_path(r'ws/echo/$', EchoConsumer.as_asgi()),
    re_path(r'ws/group_echo/$', GroupEchoConsumer.as_asgi())
]
