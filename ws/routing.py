from django.urls import re_path

from .consumers import EchoConsumer, GroupEchoConsumer, TimerEchoConsumer, ChannelEchoConsumer

websocket_urlpatterns = [
    re_path(r'ws/echo/$', EchoConsumer.as_asgi()),
    re_path(r'ws/group_echo/$', GroupEchoConsumer.as_asgi()),
    re_path(r'ws/timer_echo/$', TimerEchoConsumer.as_asgi()),
    re_path(r'ws/channel_echo/$', ChannelEchoConsumer.as_asgi())
]
