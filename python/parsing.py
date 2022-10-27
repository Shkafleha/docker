# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
import mysql.connector
import time, requests

ses = requests.Session()
ses.headers = {'HH-User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"}
vac = {'msc_anal':'analyst+удаленно&area=1',
       'msc_scienist':'scientist+удаленно&area=1',
       'spb_anal':'scientist&area=2',
       'spb_scienist':'analyst&area=2'}

result = {}
for spec in vac:
  url = f'https://api.hh.ru/vacancies?text=Data+{vac[spec]}&per_page=100&no_magic=true&ored_clusters=true&enable_snippets=true'
  print(url)
  res = ses.get(url)
  # getting a list of all pesponses
  res_all = []
  for p in range(res.json()['pages']):
      # print(f'scraping page {p}')
      url_p = url + f'&page={p}'
      res = ses.get(url_p)
      res_all.append(res.json())
      time.sleep(0.2)
  print(res_all[0]['found'])
  result[spec] = res_all[0]['found']
result


cur_time = str(time.strftime('%Y-%m-%d %H:%M:%S'))


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
insert_stmt = (
  "INSERT INTO hh (DateTimeNow, msc_anal, msc_scienist, spb_anal, spb_scienist) "
  "VALUES (%s, %s, %s, %s, %s)"
)
data = (cur_time, result['msc_anal'], result['msc_scienist'], result['spb_anal'], result['spb_scienist'])
cursor.execute(insert_stmt, data)


cursor.execute("SELECT * FROM hh")
data = cursor.fetchall()
# Make the changes to the database persistent
connection.commit()

# Close communication with the database
cursor.close()
connection.close()
print(data)
# mysqldump