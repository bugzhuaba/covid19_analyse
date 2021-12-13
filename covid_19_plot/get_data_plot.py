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
cursor.execute("DROP TABLE IF EXISTS 新增趋势")
sql='CREATE TABLE 新增趋势 (updateDate CHAR(20) NOT NULL,data_in CHAR(20),data_out CHAR(20))'
cursor.execute(sql)
print("CREATE TABLE OK")

url = "https://voice.baidu.com/act/newpneumonia/newpneumonia"
response=requests.get(url)
html=etree.HTML(response.text)
result=html.xpath('//script[@type="application/json"]/text()')
result=result[0]
result=json.loads(result)#将字符串转换为python数据类型
result_time=result['component'][0]['trend']['updateDate']
result_in=result['component'][0]['trend']['list'][10]['data']
result_out=result['component'][0]['allForeignTrend']['list'][4]['data']
i=0
for i in range(len(result_time)):
    sql='insert into 新增趋势 values(%s,%s,%s)'
    cursor.execute(sql, (result_time[i],result_in[i],result_out[i]))
    i=i+1
connection.commit()

plt.title('国内/国外新增确诊 趋势')
plt.rcParams['font.sans-serif']=['SimHei']
plt.xlabel('日期')
plt.ylabel('确诊人数')
plt.plot(result_time,result_in)
plt.plot(result_time,result_out)
plt.xticks(result_time[::10])
for a,b in zip(result_time[::5],result_in[::5]):
    plt.text(a,b,b,ha='center',va='bottom',fontsize=12)
for a,b in zip(result_time[::5],result_out[::5]):
    plt.text(a,b,b,ha='center',va='bottom',fontsize=12)
plt.savefig('新增趋势.jpg')
plt.show()
connection.close