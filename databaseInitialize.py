import pymysql

connection = pymysql.connect(
   host='localhost',
   user='root',
   password='',
   db='dns',
)

if __name__ == '__main__':
   databaseFile = open("dns.sql", "r")
   try:
       with connection.cursor() as cursor:
           sql = databaseFile.read()
           print("Database SQL Query Created")
           try:
               cursor.execute(sql)
               print("Database Created")
           except:
               print("SQL exception")
           connection.commit()
   finally:
           connection.close()
   databaseFile.close()
