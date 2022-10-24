# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': 'mysql',
  'database': 'db',
  'port': "3306"
}
connection = mysql.connector.connect(**config)
print('DB connected')
cursor = connection.cursor()
cursor.execute("insert into hh(Amount) values(25)")
print('New attempt')
cursor.execute("SELECT * FROM hh")
data = cursor.fetchall()
connection.close()
print(data)
