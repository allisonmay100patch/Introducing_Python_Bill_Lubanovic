import zmq
from datetime import datetime
import time
host = '127.0.0.1'
port = 6789
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://%s:%s" % (host,port))
while True:
    quotable = 'please send date and time'
    quote = quotable.encode('utf-8')
    request_bytes = server.recv()
    time.sleep(1)
    dt = datetime.now()
    dt_bytes = bytes(str(dt),encoding='utf-8')
    server.send(dt_bytes)
    