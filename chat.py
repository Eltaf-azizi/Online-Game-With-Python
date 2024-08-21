"""
Represent and stores information about the chat
"""

class Chat(object):

    def __init__(self):
        self.content = []

    def updatechat(self, msg):
        self.content.appenf(msg)

    def getchat(self):
        return self.content
    
    def len(self):
        return len(self.content)
    
    def str(self):
        return "".join(self.content)
    
    def repr(self):
        return str(self)