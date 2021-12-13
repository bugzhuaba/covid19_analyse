import json
import data_get
from covid_19 import map_new

with open('data.json','r')as file:
    data=file.read()
    data=json.loads(data)
map=map_new.Draw_map()
datas=data_get.Get_data()
datas.get_data()
updata_time=datas.get_time()
datas.parse_data()
#中国疫情地图数据
def china_map():
    area=[]
    confirmed=[]
    for each in data:
        area.append(each['area'])
        confirmed.append(each['curConfirm'])
        map.to_map_china(area,confirmed,updata_time)

#省份疫情数据
def province_map():
    for each in data:
        city=[]
        confirmeds=[]
        province=each['area']
        for each_city in each['subList']:
            city.append(each_city['city'])
            confirmeds.append(each_city['curConfirm'])



china_map()