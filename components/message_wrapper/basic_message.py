class MessageWrapper:

    def __init__(self, subject, content, attachments):
        self.subject = subject
        self.content = content
        self.attachments = attachments


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
        return self.__attachments
