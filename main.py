import twitter
import parser
import random

from time import sleep

from threading import Timer

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.function   = function
        self.interval   = interval
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

posted = []

def run():
    if len(posted) < len(parser.sentences):
        k = random.choice(parser.sentences)
        if k not in posted:
            posted.append(k)
            api.PostUpdates(k)
        else:
            run()


rt = RepeatedTimer(3600, run) # it auto-starts, no need of rt.start()
try:
    sleep(60000) # your long-running job goes here...
finally:
    rt.stop() # better in a try/finally block to make sure the program ends!
