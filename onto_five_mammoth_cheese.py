import zmq
host = '127.0.0.1'
port = 6789
ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)



sub.connect('tcp://%s:%s' % (host,port))
sub.setsockopt(zmq.SUBSCRIBE,b'')

cb=str()
while True:
    cheese_byte = sub.recv()
    cb = str(cheese_byte.decode())
    i = len(cb)
    if i == 5:
        print(cheese_byte)
