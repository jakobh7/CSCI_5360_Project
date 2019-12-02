#code from PubNub blog https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/
from socket import *
from io import BytesIO
from http import server
import pymysql

connection = pymysql.connect(
   host='localhost',
   user='root',
   password='',
   db='dns',
)

class RequestHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_content("Hello")

    def send_content(self, content):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Content-length", str(len(content)))
        self.end_headers()
        send.wfile.write(content)


if __name__ == '__main__':
   serverAddress = ('', 8080)
   server = server.HTTPServer(serverAddress, RequestHandler)
   print("Serving on Port 8080...")
   server.serve_forever()
