from django.urls import re_path

from .consumers import EchoConsumer

websocket_urlpatterns = [
    re_path(r'ws/tick_tock/$', EchoConsumer.as_asgi())
]
