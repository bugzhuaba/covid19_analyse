from pyecharts import options as opts
from pyecharts.charts import Map
from  pyecharts.faker import Faker


class Draw_map():

    def to_map_china(self,area ,variate,updata_time):
        pieces=[
            # {'max':999999,"min":100000,'lable':'>100000','color':'#8A0808'},
            {'max':99999,"min":10000,'lable':'>10000','color':'#8A0808'},
            {'max':9999,"min":1000,'lable':'1000-9999','color':'#B40404'},
            {'max':999,"min":100,'lable':'100-999','color':'#DF0101'},
            {'max':99,"min":10,'lable':'10-99','color':'#F65152'},
            {'max':9,"min":1,'lable':'0-9','color':'#F5A9A9'},
            {'max':0,"min":0,'lable':'0','color':'#FFFFFF'},

        ]
        c=(
            Map(init_opts=opts.InitOpts(width='1000px',height='880px'))
            .add("累计确诊人数",[list(z) for z in zip (area,variate)], "china")
            .set_global_opts(
                title_opts=opts.TitleOpts(title="中国疫情地图分布",subtitle='截止%s 中国疫情分布情况'%(updata_time)
                                          ,pos_right='center',pos_top='30px'),
                visualmap_opts=opts.VisualMapOpts(max_=200,is_piecewise=True,pieces=pieces),

            )
            .render("中国疫情地图.html")
        )

