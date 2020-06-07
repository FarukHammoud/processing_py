from threading import Thread, Event
import sys
class Listener(Thread):
    def __init__(self,channel,isDead):
        Thread.__init__(self)
        self.isDead = isDead
        self.channel = channel
        self.start()
    def run(self):
        while(not self.isDead.isSet()):
            msg = self.channel.readline().decode('utf-8')
            if msg != '':
                print('>> '+msg,file=sys.stderr)
                
    