import email

from server_wrapper.base_server import BaseServerWrapper as smtp

class Service:

    def __init__(self, message_obj):
        self.message_obj = message_obj


    def build_message(self):
        pass
