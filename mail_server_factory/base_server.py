import smtplib, ssl


class BaseServerWrapper:

    def __init__(self, smtp_server, port, account, password):
        self.smtp_server = smtp_server
        self.port = port
        self.account = account
        self.password = password
    

    def send_email(self, sender, receivers, message):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as smtp:
            smtp.login(self.account, self.password)
            smtp.sendmail(sender, receivers, message)
