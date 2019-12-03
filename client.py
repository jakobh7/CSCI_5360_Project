from socket import *
from io import BytesIO
from http import client

conn = client.HTTPConnection("localhost", 8080)
conn.request("GET", "/?name=slu.edu")
response = conn.getresponse()
print(response.read().decode('utf-8'))
print(response.status)

conn.request("GET", "/?badinput=slu.edu")
response = conn.getresponse()
print(response.read().decode('utf-8'))
print(response.status)

conn.request("GET", "/?name=bar.bad")
response = conn.getresponse()
print(response.read().decode('utf-8'))
print(response.status)
