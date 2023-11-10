import zmq
import time
host = '127.0.0.1'
port = 6789
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect("tcp://%s:%s" % (host, port))
send_str = 'please send date and time'
request_bytes = send_str.encode('utf-8')
client.send(request_bytes)
reply_bytes = client.recv()
rb=reply_bytes.decode('utf-8')
print('Sent %s, received %s' % (send_str,rb))