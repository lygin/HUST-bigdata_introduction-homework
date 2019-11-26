# -*-coding:utf-8-*-
import pygal
from 文件合并处理 import ave_prices,deal_num,subway_price
from 数据分析处理 import floor_price,app_price,house_num,house_type,monthlydeal_num,month_num,monthlydeal_num18,month_num18,household_num,household,scatter
from pygal.style import DarkSolarizedStyle
from pygal.style import NeonStyle
from pygal.style import TurquoiseStyle

# 对结果进行可视化
import pygal
line_chart = pygal.HorizontalBar(width=1100,fill=True, interpolate='cubic')
line_chart.title = '武汉各区租房每平米价格'
line_chart.add('东西湖区', ave_prices[0])
line_chart.add('新洲区', ave_prices[1])
line_chart.add( '江岸区', ave_prices[2])
line_chart.add('江汉区', ave_prices[3])
line_chart.add('蔡甸区', ave_prices[4])
line_chart.add('青山区', ave_prices[5])
line_chart.add('硚口区',ave_prices[6])
line_chart.add('汉阳区',ave_prices[7])
line_chart.add('江夏区',ave_prices[8])
line_chart.add('黄陂区',ave_prices[9])
line_chart.add('武昌区',ave_prices[10])
line_chart.add('洪山区',ave_prices[11])
line_chart.x_title="每平米价格"
line_chart.render_to_file("武汉各区租房每平米价格.svg")

hist = pygal.Bar(width=1100,fill=True, interpolate='cubic')
hist.title = "武汉各区租房每平米价格对比"
hist.x_labels = ['东西湖区', '新洲区', '江岸区', '江汉区', '蔡甸区', '青山区','硚口区','汉阳区','江夏区','黄陂区','武昌区','洪山区']
hist.x_title = "区域"
hist.y_title = "每平米单价"
hist.add('武汉', ave_prices)
hist.render_to_file('各区每平米价格.svg')

hist = pygal.Bar(width=1100,fill=True, interpolate='cubic')
hist.title = "武汉各区租房2019年成交数"
hist.x_labels = ['东西湖区', '新洲区', '江岸区', '江汉区', '蔡甸区', '青山区','硚口区','汉阳区','江夏区','黄陂区','武昌区','洪山区']
hist.x_title = "区域"
hist.y_title = "成交数量"
hist.add('武汉', deal_num)
hist.render_to_file('各区交易量.svg')

hist = pygal.Bar(width=1100,fill=True, interpolate='cubic')
hist.title = "地铁或上下楼便利性对房价的影响"
hist.x_labels = ["便利",'不便利']
hist.y_title = "每平米单价"
hist.add('地铁', subway_price)
hist.add('上下楼',floor_price)
hist.render_to_file('便利性影响 .svg')


hist = pygal.Bar(width=1100,fill=True, interpolate='cubic')
hist.title = "家庭设施（电视，冰箱，洗衣机，空调，热水器，床，暖气，宽带，天然气）对房价的影响"
hist.x_labels = ['有0-2项', '有2-4项', '有4-6项', '有6-9项']
hist.x_title = "家庭设施拥有的项数"
hist.y_title = "每平米单价"
hist.add('武汉', app_price)
hist.render_to_file('家庭设施影响.svg')

line_chart = pygal.HorizontalBar(width=1100,fill=True, interpolate='cubic')
line_chart.title = '武汉租房各种类数量统计'
line_chart.add('武汉', house_num)
line_chart.x_labels=house_type
line_chart.render_to_file("租房各种类数量统计.svg")

#2019年各月上架额
line_chart = pygal.Line(width=1100,fill=True, interpolate='cubic')
line_chart.title = '2019年各月上架额'
line_chart.x_labels =month_num
line_chart.add('2019', monthlydeal_num)
line_chart.render_to_file("2019年各月上架额.svg")

#2018年各月上架额
line_chart = pygal.Line(width=1100,fill=True, interpolate='cubic')
line_chart.title = '2018年各月上架额'
line_chart.x_labels =month_num18
line_chart.add('2018', monthlydeal_num18)
line_chart.render_to_file("2018年各月上架额.svg")

#各区上架量在武汉的占比
pie_chart = pygal.Pie(inner_radius=.4)
pie_chart.title = '各区上架量在武汉的占比( %)'
pie_chart.add('东西湖区', deal_num[0])
pie_chart.add('新洲区',deal_num[1] )
pie_chart.add('江岸区', deal_num[2])
pie_chart.add('江汉区', deal_num[3])
pie_chart.add('蔡甸区', deal_num[4])
pie_chart.add('青山区', deal_num[5])
pie_chart.add('硚口区', deal_num[6])
pie_chart.add('汉阳区', deal_num[7])
pie_chart.add('江夏区', deal_num[8])
pie_chart.add('黄陂区',deal_num[9])
pie_chart.add('武昌区',deal_num[10])
pie_chart.add('洪山区',deal_num[10])
pie_chart.render_to_file("各区上架量在武汉的占比.svg")

#租房各家庭设施的出现率比较
radar_chart = pygal.Radar(fill=True)
radar_chart.title = '租房各家庭设施的出现率'
radar_chart.x_labels = household
radar_chart.add('武汉', household_num)
radar_chart.render_to_file("租房各家庭设施的出现率.svg")

#date-price scatter plot
xy_chart = pygal.XY(width=1100,fill=True, interpolate='cubic',stroke=False)
xy_chart.title = '从2018年至今租房价格散点图'
xy_chart.add('武汉', scatter)
xy_chart.y_title = "元/每平米"
xy_chart.x_labels=['2018-06-01','2018-09-01','2018-12-01','2019-03-01','2019-06-01']
xy_chart.render_to_file("时间房价散点图.svg")