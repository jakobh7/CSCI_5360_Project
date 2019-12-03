#code from PubNub blog https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/
from socket import *
from io import BytesIO
from http import server
import pymysql
import json

connection = pymysql.connect(
   host='localhost',
   user='root',
   password='',
   db='dns',
)

##sql = f"INSERT INTO records (`Name`, `Value`, `Type`, `TTL`) VALUES (\"{record_name}\", \"{record_value}\", \"{record_type}\", {record_TTL})"

class RequestHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        ##TODO: Implement parsing get request and SQL queries to data
        self.send_content({'foo':'bar'})

    def send_content(self, content):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Content-length", str(len(json.dumps(content))))
        self.end_headers()
        self.wfile.write(json.dumps(content).encode('utf-8'))


if __name__ == '__main__':
   serverAddress = ('', 8080)
   server = server.HTTPServer(serverAddress, RequestHandler)
   print("Serving on Port 8080...")
   server.serve_forever()
