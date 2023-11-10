from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime
def now():
   return datetime.now()

server = SimpleXMLRPCServer(('localhost',6789))
server.register_function(now)
server.serve_forever()

