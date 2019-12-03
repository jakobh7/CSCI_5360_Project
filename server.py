from socket import *
from io import BytesIO
from http import server
import pymysql
import json

class RequestHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        name = ""
        namefound = False
        returnvalue = ""
        linesreturned = -1
        error_code = 200
        returnjson = {}

        request_data = self.path[1:]
        values = request_data.split('?')

        for value in values:
            print(value)
            key_value = value.split('=')
            if(key_value[0]=="name"):
                name = key_value[1]
                namefound = True

        if not namefound:
            error_code = 400
            returnjson["Error"] = "Request Formatted improperly"
        else:
           try:
               connection = pymysql.connect(
                  host='localhost',
                  user='root',
                  password='',
                  db='dns',
               )
               with connection.cursor() as cursor:
                   sql = f"SELECT * FROM records WHERE `name` = \"{name}\""
                   print("Select Query: ", sql)
                   try:
                       linesreturned = cursor.execute(sql)
                       if linesreturned == 1:
                          returnvalue = cursor.fetchall()
                          for line in returnvalue:
                             returnjson["name"] = line[0]
                             returnjson["ipaddress"] = line[1]
                       else:
                          error_code = 404
                          returnjson["Error"] = "Hostname not found in DNS database"
                   except:
                       print("SQL error")
                       error_code = 500
                       returnjson["Error"] = "SQL connection issue"
                   connection.commit()
           finally:
               connection.close()

        self.send_content(returnjson, error_code)

    def send_content(self, content, error_code=200):
        self.send_response(error_code)
        self.send_header("Content-type", "application/json")
        self.send_header("Content-length", str(len(json.dumps(content))))
        self.end_headers()
        self.wfile.write(json.dumps(content).encode('utf-8'))


if __name__ == '__main__':
   serverAddress = ('', 8080)
   server = server.HTTPServer(serverAddress, RequestHandler)
   print("Serving on Port 8080...")
   server.serve_forever()
