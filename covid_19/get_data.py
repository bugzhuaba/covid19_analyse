import requests
from lxml import etree
import json
import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='covid_19',)
cursor=connection.cursor()
cursor.execute("DROP TABLE IF EXISTS 中国")
sql='CREATE TABLE 中国 (area CHAR(20) NOT NULL,confirmed CHAR(20),died CHAR(20),crued CHAR(20),curConfirm CHAR(20),confirmedRelative CHAR(20),diedRelative CHAR(20),curedRelative CHAR(20),curConfirmRelative CHAR(20))'
cursor.execute(sql)
print("CREATE TABLE OK")

url = "https://voice.baidu.com/act/newpneumonia/newpneumonia"
response=requests.get(url)
html=etree.HTML(response.text)
result=html.xpath('//script[@type="application/json"]/text()')
result=result[0]
result=json.loads(result)#将字符串转换为python数据类型
result_in=result['component'][0]['caseList']
result_out=result['component'][0]['globalList']
for each in result_in:
   temp_list=[each['area'],each['confirmed'],each['died'],each['crued'],each['curConfirm'],each['confirmedRelative'],each['diedRelative'],each['curedRelative'],each['curConfirmRelative']]
   for i in range(len(temp_list)):
      if temp_list[i]=='':
         temp_list[i]='0'
   sql='insert into 中国 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
   cursor.execute(sql,(temp_list))
connection.commit()

for each in result_out:
   cursor.execute("DROP TABLE IF EXISTS "+each['area'])
   sql = 'CREATE TABLE '+each['area']+'(country CHAR(50) NOT NULL,confirmed CHAR(20),died CHAR(20),crued CHAR(20),curConfirm CHAR(20),confirmedRelative CHAR(20))'
   cursor.execute(sql)
   for country in each['subList']:
      temp_list=[country['country'],country['confirmed'],country['died'],country['crued'],
                 country['curConfirm'],country['confirmedRelative']]
      for i in range(len(temp_list)):
         if temp_list[i] == '':
            temp_list[i] = '0'
      sql = 'insert into '+each['area']+' values(%s,%s,%s,%s,%s,%s)'
      # print(sql)
      cursor.execute(sql, (temp_list))
   connection.commit()
connection.close



