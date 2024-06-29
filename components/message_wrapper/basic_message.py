class MessageWrapper:

    def __init__(self, subject, content, attachments, sender, receivers):
        self.subject = subject
        self.content = content
        self.attachments = attachments
        self.sender = sender
        self.receivers = receivers


    @property
    def subject(self):
        return self.__subject
    
    @subject.setter
    def subject(self, subject):
        if len(subject) == 0:
            raise Exception('The subject cannot be empty!')
        self.__subject = subject

    
    @property
    def content(self):
        return self.__content
    
    @content.setter
    def content(self, content):
        self.__content = content
    

    @property
    def attachments(self):
        return self.__attachments
    
    @attachments.setter
    def attachments(self, attachments):
        self.__attachments = attachments


    @property
    def sender(self):
        return self.__sender
    
    @sender.setter
    def sender(self, sender):
        if len(sender) == 0:
            raise Exception('There must be a sender!')
        self.__sender = sender
    

    @property
    def receivers(self):
        return self.__receivers
    
    @receivers.setter
    def receivers(self, receivers):
        if len(receivers) == 0:
            raise Exception('There must be receivers to the email!')
        self.__receivers = receivers
