import requests;
from lxml import etree
import json
import pymysql
import os
import sys
from pytz import unicode

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='covid_19',)
cursor=connection.cursor()
cursor.execute("DROP TABLE IF EXISTS 疫苗")
sql='CREATE TABLE 疫苗 (country CHAR(20) NOT NULL,date CHAR(20),vaccinebrands CHAR(80),total CHAR(20),per_hundred CHAR(20))'
cursor.execute(sql)
print("CREATE TABLE OK")
url='https://health.ifeng.com/c/special/85mhVvWS5i4'
response=requests.get(url)
response.content.decode("utf-8")
html=etree.HTML(response.text)
result=html.xpath('//script/text()')
result=result[5]
result=result.lstrip()
with open("vaccines.txt","w") as f:
    f.write(result)

lines = open('vaccines.txt').readlines() #打开文件，读入每一行
fp = open('vaccines.txt','w')
for s in lines:
    fp.write(s.replace('var allData = ','')) # replace是替换，write是写入
fp.close() # 关闭文件

with open('vaccines.txt','r') as file:
    result = file.read()
result=json.dumps(result)
result=json.loads(result)#将字符串转换为python数据类型
print(result)
print(type(result))
# result=result['area']

# # result_out=result['component'][0]['globalList']
# print(result)
# result=result[0]
# result=json.loads(result)#将字符串转换为python数据类型
# result=result['area'][0]
# for each in result_in:
#    temp_list=[each['area'],each['confirmed'],each['died'],each['crued'],each['curConfirm'],each['confirmedRelative'],each['diedRelative'],each['curedRelative'],each['curConfirmRelative']]
#    for i in range(len(temp_list)):
#       if temp_list[i]=='':
#          temp_list[i]='0'
#    sql='insert into 中国 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#    cursor.execute(sql,(temp_list))
# connection.commit()
#
# for each in result_out:
#    cursor.execute("DROP TABLE IF EXISTS "+each['area'])
#    sql = 'CREATE TABLE '+each['area']+'(country CHAR(50) NOT NULL,confirmed CHAR(20),died CHAR(20),crued CHAR(20),curConfirm CHAR(20),confirmedRelative CHAR(20))'
#    cursor.execute(sql)
#    for country in each['subList']:
#       temp_list=[country['country'],country['confirmed'],country['died'],country['crued'],
#                  country['curConfirm'],country['confirmedRelative']]
#       for i in range(len(temp_list)):
#          if temp_list[i] == '':
#             temp_list[i] = '0'
#       sql = 'insert into '+each['area']+' values(%s,%s,%s,%s,%s,%s)'
#       # print(sql)
#       cursor.execute(sql, (temp_list))
#    connection.commit()
# connection.close