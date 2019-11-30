#code from PubNub blog https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/
from socket import *
from io import BytesIO
from http import client

conn = client.HTTPConnection("localhost", 8080)
conn.request("GET", "/")
response = conn.getresponse()
print(response)

'''
text = "I am CLIENT\n"
bytes_text = bytes(text, 'utf-8')

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

client.send(bytes_text)

bytes_from_server=client.recv(4096)

client.close()

from_server = bytes_from_server.decode('utf-8')

print(from_server)
'''
