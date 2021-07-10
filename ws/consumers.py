import random
import string
import asyncio
import redis
from django.conf import settings
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.exceptions import StopConsumer

redis_connection = redis.Redis(settings.REDIS_HOST, settings.REDIS_PORT)


class EchoConsumer(WebsocketConsumer):
    """Потребитель, отвечающий эхо-сообщением на каждое поступившее сообщение от клиента"""

    def __init__(self):
        self.count = 0
        WebsocketConsumer.__init__(self)

    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        self.count += 1
        self.send(f'echo_{self.count}')

    def disconnect(self, code):
        raise StopConsumer


class GroupEchoConsumer(AsyncWebsocketConsumer):
    """Потребитель, рассылающий  приходящие сообщения всем членам группы"""
    groups = ['broadcast']

    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        await self.channel_layer.group_send(
            'broadcast',
            {
                'type': 'group.message',
                'message': text_data
            }
        )

    async def group_message(self, event):
        await self.send(event['message'])

    async def disconnect(self, code):
        raise StopConsumer


class TimerEchoConsumer(AsyncWebsocketConsumer):
    """Потребитель, отсылающий по таймеру несколько сообщений в ответ на пришедший фрейм"""

    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        echo_key = random.choice(string.ascii_uppercase) + random.choice('0123456789')
        for i in range(10):
            await self.send(text_data=f'echo_{i + 1}_{echo_key}')
            await asyncio.sleep(0.5)

    async def disconnect(self, code):
        raise StopConsumer


class ChannelEchoConsumer(AsyncWebsocketConsumer):
    """Потребитель, пересылающий сообщения только указанному адресату"""
