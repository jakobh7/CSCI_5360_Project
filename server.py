from socket import *
from io import BytesIO
from http import server
import pymysql
import json
import hasher

class RequestHandler(server.BaseHTTPRequestHandler):
    def do_POST(self):
        headers_json = self.headers
        returnjson = {}
        returnjson["Hello"] = "World"
        data_json = {}
        questions = {}
        answers = {}
        authority = {}
        additional_info = {}
        name = ""
        error_code = 200

        try:
            print(headers_json)
            content_length = int(headers_json["Content-Length"])
            ID = headers_json["Identification"]
            headers_json["ControlFlags"] = "100010000000000"
            question_count = headers_json["QuestionCount"]
            answer_count = headers_json["AnswerCount"]
            authority_count = headers_json["AuthorityCount"]
            additional_count = headers_json["AdditionalCount"]


            data = self.rfile.read(content_length)
            data_json = json.loads(data.decode('utf-8'))
            print(data_json)
            questions = data_json["Questions"]
            print("Extracted Questions: ", questions)
            answers = data_json["Answers"]
            print("Extracted Answers: ", answers)
            authority = data_json["Authority"]
            print("Extracted Authority: ", authority)
            additional_info = data_json["AdditionalInfo"]
            print("Extracted Additional Info: ", additional_info)

            name = questions["Name"]
            print("data extracted", name)
        except:
            print("400 error")
            error_code = 400
            returnjson["Error"] = "Request Formatted improperly"

        if error_code == 200:
          try:
              connection = pymysql.connect(
                 host='localhost',
                 user='root',
                 password='',
                 db='dns',
              )
              with connection.cursor() as cursor:
                   sql = f"SELECT * FROM records WHERE `Name` = \"{name}\""
                   print("Select Query: ", sql)
                   try:
                       linesreturned = cursor.execute(sql)
                       headers_json["AnswerCount"] = linesreturned
                       if linesreturned == 1:
                           returnvalue = cursor.fetchall()
                           for line in returnvalue:
                               answers["Name"] = line[0]
                               answers["Value"] = line[1]
                               answers["Type"] = line[2]
                               answers["TTL"] = line[3]

                       else:
                           error_code = 404
                           data_json["Error"] = "Hostname not resolved in DNS database"

                   except:
                       print("SQL error")
                       error_code = 500
                       data_json["Error"] = "SQL connection issue"

                   connection.commit()
          finally:
              connection.close()

          hash = hasher.AESEncrypt(32, '{', b"5VVMUS6P89TNH2AHD178KG2S7QIE7ICJ")
          additional_info["Hash"] = hash.encode(answers["Name"])
          self.send_content(data_json, error_code)

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
