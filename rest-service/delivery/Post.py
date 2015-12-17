import json, random, pprint

class Post(object):

    def __init__(self):
        self.initMessages()
        #self.mobs = []

    def initMessages(self):
        with open('delivery/messages.json', 'r') as messages_list:
            self.messages = json.load(messages_list)

    def printAllMessages(self):
        return json.dumps(self.messages)

    def getMessageFrom(self, monster):
        for msg in self.messages['msg_list']:
            if msg['from'] == monster:
                return msg
        return "No message found from " + monster

    def getMessageTo(self, monster):
        for msg in self.messages['msg_list']:
            if msg['to'] == monster:
                return json.dumps(msg)
        return "No message found from " + monster
