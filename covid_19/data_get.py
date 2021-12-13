import  requests
from lxml import  etree
import re
import json

class Get_data():
    def get_data(self):#获取数据

        response=requests.get('https://voice.baidu.com/act/newpneumonia/newpneumonia')
        with open('html.txt','w')as file:
            file.write(response.text)

    # 获取时间
    def get_time(self):
        with open('html.txt','r')as file:
            text = file.read()
        time=re.findall('"mapLastUpdatedTime":"(.*?)"',text)[0]
        return (time)

    def parse_data(self):#解析数据
        with open('html.txt','r')as file:
            text=file.read()
        html=etree.HTML(text)
        result=html.xpath('//script[@type="application/json"]/text()')
        result=result[0]
        result=json.loads(result)
        result=result['component'][0]['caseList']
        result=json.dumps(result)
        with open('data.json',"w") as file:
            file.write(result)
            print('数据已写入json文件')








