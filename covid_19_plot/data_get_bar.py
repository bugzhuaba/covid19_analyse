import requests;
from lxml import etree
import json
import pymysql
import matplotlib.pyplot as plt

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='covid_19',)
cursor=connection.cursor()
cursor.execute("DROP TABLE IF EXISTS 新增确诊国家Top10")
sql='CREATE TABLE 新增确诊国家Top10 (country CHAR(50) NOT NULL,data CHAR(20))'
cursor.execute(sql)
print("CREATE TABLE OK")

url = "https://voice.baidu.com/act/newpneumonia/newpneumonia"
response=requests.get(url)
html=etree.HTML(response.text)
result=html.xpath('//script[@type="application/json"]/text()')
result=result[0]
result=json.loads(result)#将字符串转换为python数据类型
result=result['component'][0]['topAddCountry']
country=[]
num=[]
for each in result:
   temp_list=[each['name'],each['value']]
   country+=[each['name']]
   num+=[each['value']]
   sql='insert into 新增确诊国家Top10 values(%s,%s)'
   cursor.execute(sql,(temp_list))
connection.commit()


fig=plt.figure()
plt.rcParams['font.sans-serif']=['SimHei']
plt.bar(country,num,color='red')
plt.xlabel('国家')
plt.ylabel('新增确诊数')
for a,b in zip(country,num):
    plt.text(a,b,b,ha='center',va='bottom',fontsize=12)
plt.title('新增确诊国家Top10')
plt.savefig('新增确诊国家Top10.jpg')
plt.show()

connection.close