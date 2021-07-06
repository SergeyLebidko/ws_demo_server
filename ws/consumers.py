from channels.generic.websocket import WebsocketConsumer
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
