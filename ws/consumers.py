from channels.generic.websocket import WebsocketConsumer


class EchoConsumer(WebsocketConsumer):

    def connect(self):
        print('Connect')
        self.accept()

    def disconnect(self, code):
        print('Disconnect with code', code)
