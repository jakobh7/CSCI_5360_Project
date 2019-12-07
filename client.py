from socket import *
from io import BytesIO
from http import client
import json
import hasher


headers = {}
ID = 1#getRandomBits
ControlFlags = "000010000000000"
QuestionCount = 1
AnswerCount = 0
AuthorityCount = 0
AdditionalCount = 0

headers["Content-Type"] = "application/json"
headers["Identification"] = ID
headers["ControlFlags"] = ControlFlags
headers["QuestionCount"] = QuestionCount
headers["AnswerCount"] = AnswerCount
headers["AuthorityCount"] = AuthorityCount
headers["AdditionalCount"] = AdditionalCount

resource_records = {}
questions = {}
questions["Name"] = "slu.edu"
questions["Type"] = "A"
answers = {}
authority = {}
additional_info = {}
resource_records["Questions"] = questions
resource_records["Answers"] = answers
resource_records["Authority"] = authority
resource_records["AdditionalInfo"] = additional_info

headers["Content-Length"] = len(json.dumps(resource_records))

conn = client.HTTPConnection("localhost", 8080)
conn.request("POST", "/", json.dumps(resource_records).encode('utf-8'), headers)
response = conn.getresponse()
print(response.read().decode('utf-8'))
hash = hasher.AESEncrypt(32, '{', b"5VVMUS6P89TNH2AHD178KG2S7QIE7ICJ")
print("Comparing Endoded hashes", hash.encode(questions["Name"]))
print(response.status)

'''
conn.request("GET", "/?badinput=slu.edu")
response = conn.getresponse()
print(response.read().decode('utf-8'))
print(response.status)

conn.request("GET", "/?name=bar.bad")
response = conn.getresponse()
print(response.read().decode('utf-8'))
print(response.status)
'''
