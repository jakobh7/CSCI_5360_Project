#code from PubNub blog https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/
from socket import *
from io import BytesIO
from http import client

conn = client.HTTPConnection("localhost", 8080)
conn.request("GET", "/")
response = conn.getresponse()
print(response)
