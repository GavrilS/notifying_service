"""
This file is responsible for running the entire project based on the specified user settings.

Usage:
python3 engine.py
python3 core/engine.py --smtp_server '' --smtp_port '' --smtp_acc '' --smtp_acc_pass ''
"""
from argparse import ArgumentParser
from mail_server_factory.base_server import BaseServerWrapper
from components.notifying_service import Service
from components.message_wrapper.basic_message import MessageWrapper


def main(**kwargs):
    # Build the message
    message_subject = 'Test email notification'
    message_body = 'This is a test on the email notification service'
    sender = 'gavr1lll@abv.bg'
    receivers = [
        'gsamodivekov@gmail.com'
    ]

    m = MessageWrapper(message_subject, message_body, None, sender, receivers)

    # Setup the smtp server
    server = kwargs.get('smtp_server')
    port = kwargs.get('smtp_port')
    account = kwargs.get('smtp_acc')
    password = kwargs.get('smtp_acc_pass')

    print(f"Server: {server}\nPort: {port}\nAcc: {account}\nPassword: {password}")

    smtp = BaseServerWrapper(server, port, account, password)

    # Setup the notifying service and send the email
    notify_service = Service(m, smtp)
    notify_service.send_email()


if __name__=='__main__':
    parser = ArgumentParser(description='Provide the necessary data to connect to the SMTP server.')
    parser.add_argument('--smtp_server')
    parser.add_argument('--smtp_port')
    parser.add_argument('--smtp_acc')
    parser.add_argument('--smtp_acc_pass')

    args = parser.parse_args()
    smtp_server = args.smtp_server
    smtp_port = args.smtp_port
    smtp_acc = args.smtp_acc
    smtp_acc_pass = args.smtp_acc_pass
    main(
        smtp_server=smtp_server, 
        smtp_port=smtp_port, 
        smtp_acc=smtp_acc, 
        smtp_acc_pass=smtp_acc_pass
    )
