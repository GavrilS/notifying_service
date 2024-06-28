import smtplib


class BaseServerWrapper:

    def __init__(self, smtp_server, port):
        self.smtp_server = smtp_server
        self.port = port

    
    def connect_to_server(self):
        smtp = smtplib.SMTP.connect(self.smtp_server, self.port)
        return smtp
