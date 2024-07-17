# import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class Service:

    def __init__(self, message_obj, smpt_server):
        self.__message_obj = message_obj
        self.__smtp_server = smpt_server


    @property
    def message_obj(self):
        return self.__message_obj
    

    @property
    def smtp_server(self):
        return self.__smtp_server


    def reload_message(self, message_obj):
        self.__message_obj = message_obj


    def reload_smtp_server(self, smtp_server):
        self.__smtp_server = smtp_server


    def prepare_email_with_attachments(self):
        # Create multipart message and set headers
        message = MIMEMultipart()
        self._set_message_headers(message)

        # Add body to the email
        message.attach(MIMEText(self.message_obj.content, 'plain'))

        # Specify file attachments
        for file in self.message_obj.attachments:
            with open(file, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            
            # Encode file in ASCII characters to send with the email
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename={file}")

            # Add attachment to message
            message.attach(part)
        
        return message
    

    def prepare_email(self):
        # Create MIMEText object
        message = MIMEText(self.message_obj.content, 'plain')
        self._set_message_headers(message)

        return message

    
    def _set_message_headers(self, message):
        message['Subject'] = self.message_obj.subject
        message['From'] = self.message_obj.sender
        message['To'] = self.message_obj.receivers
    

    def send_email(self):
        if self.message_obj.attachments and len(self.message_obj.attachments) > 0:
            message = self.prepare_email_with_attachments()
        else:
            message = self.prepare_email()

        self.smtp_server.send_email(message)
