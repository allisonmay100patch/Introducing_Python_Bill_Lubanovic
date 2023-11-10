import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
result = proxy.now()
print('The current date and time:',result)