"""
This file is responsible for running the entire project based on the specified user settings.

Usage:
python3 engine.py
"""
from mail_server_factory.base_server import BaseServerWrapper
from components.notifying_service import Service
from components.message_wrapper.basic_message import MessageWrapper


def main():
    # Build the message
    message_subject = 'Test email notification'
    message_body = 'This is a test on the email notification service'
    sender = 'gavr1lll@abv.bg'
    receivers = [
        'gsamodivekov@gmail.com'
    ]

    m = MessageWrapper(message_subject, message_body, None, sender, receivers)

    # Setup the smtp server
    server = 'smtp.abv.bg'
    port = 465
    account = 'gavr1lll@abv.bg'
    password = ''

    smtp = BaseServerWrapper(server, port, account, password)

    # Setup the notifying service and send the email
    notify_service = Service(m, smtp)
    notify_service.send_email()


if __name__=='__main__':
    main()
