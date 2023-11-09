import zmq
host = '127.0.0.1'
port = 6789
ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)



sub.connect('tcp://%s:%s' % (host,port))
sub.setsockopt(zmq.SUBSCRIBE,b'')


while True:
    cheese_byte = sub.recv()
    cb = str(cheese_byte.decode())
    if cb.startswith(('a','e','i','o','u')):
        print(cb)
    if cheese_byte == None:
        sub.close()