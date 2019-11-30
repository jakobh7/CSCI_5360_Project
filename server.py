#code from PubNub blog https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/
from socket import *
from io import BytesIO
from http import server

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
   server.serve_forever()
   print("Serving on Port 8080...")

'''
text = "I am SERVER\n"
bytes_text = bytes(text, 'utf-8')

serv = socket(AF_INET, SOCK_STREAM)

serv.bind(('127.0.0.1', 8080))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    from_client = ''

    while True:
        bytes_data = conn.recv(4096)
        if not bytes_data: break
        data = bytes_data.decode('utf-8')
        from_client += data
        print(from_client)

        conn.send(bytes_text)

    conn.close()
    print('client disconnected')
    '''
