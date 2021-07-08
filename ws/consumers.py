from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.exceptions import StopConsumer


class EchoConsumer(WebsocketConsumer):

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
