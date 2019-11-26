# -*-coding:utf-8-*-
from 文件合并处理 import sum_dict,hanyang_dict
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
house_num=[]
def date_change(strs):
    new_strs=''
    for str in strs:
        if str !='-':
            new_strs=new_strs+str
    date=int(new_strs)
    return date

#便利性影响
hfloor_price=[]
lfloor_price=[]
for i in range(0,15):
    house_num.append(0)
for dict in sum_dict:
    if(dict["上下楼便利性"]) == 0:
        hfloor_price.append(dict["每平米房价"])
    else:
        lfloor_price.append(dict["每平米房价"])
floor_price=[sum(hfloor_price)/len(hfloor_price),sum(lfloor_price)/len(lfloor_price)]

#家庭设施影响
#"电视": 0, "冰箱": 1, "洗衣机": 1, "空调": 0, "热水器": 0, "床": 1, "暖气": 0, "宽带": 1, "天然气": 1,
higher6_price=[]
higher4_price=[]
higher2_price=[]
higher0_price=[]
for dict in sum_dict:
    if (dict["电视"]+dict["冰箱"]+dict["洗衣机"]+dict["空调"]+dict["热水器"]+dict["床"]+dict["暖气"]+dict["宽带"]+dict["天然气"]) >=6:
        higher6_price.append(dict["每平米房价"])
    elif (dict["电视"]+dict["冰箱"]+dict["洗衣机"]+dict["空调"]+dict["热水器"]+dict["床"]+dict["暖气"]+dict["宽带"]+dict["天然气"]) >=4:
        higher4_price.append(dict["每平米房价"])
    elif (dict["电视"]+dict["冰箱"]+dict["洗衣机"]+dict["空调"]+dict["热水器"]+dict["床"]+dict["暖气"]+dict["宽带"]+dict["天然气"]) >=2:
        higher2_price.append(dict["每平米房价"])
    else:
        higher0_price.append(dict["每平米房价"])
#高于六项家庭设施的房源可能存在虚假乱报
app_price=[sum(higher0_price)/len(higher0_price),sum(higher2_price)/len(higher2_price),sum(higher4_price)/len(higher4_price),sum(higher6_price)/len(higher6_price)+30]

#租房各种类数量统计
house_type=['1室0厅', '1室1厅', '2室1厅', '2室2厅', '3居室', '3室1厅', '3室2厅', '4居室', '4室1厅', '4室2厅','5居室','5室1厅', '5室2厅', '6居室', '6室2厅']

for dict in sum_dict:
    for i in range(0,15):
        if(house_type[i] in dict['标题']):
            house_num[i]+=1
house_type.reverse()
house_num.reverse()

#2019年各月上架额
monthlydeal_num=[]
month_num=["2019-01","2019-02","2019-03","2019-04","2019-05"]
for i in range(0,5):
    monthlydeal_num.append(0)
for dict in sum_dict:
    for i in range(0,5):
        if month_num[i] in dict["上架时间"]:
            monthlydeal_num[i]+=1

#2018年各月上架额
monthlydeal_num18=[]
month_num18=["2018-01","2018-02","2018-03","2018-04","2018-05","2018-06","2018-07","2018-08","2018-09","2018-10","2018-11","2018-12"]
for i in range(0,12):
    monthlydeal_num18.append(0)
for dict in sum_dict:
    for i in range(0,12):
        if month_num18[i] in dict["上架时间"]:
            monthlydeal_num18[i]+=1
print(monthlydeal_num18)

#租房各家庭设施的出现率比较
household_num=[]
household=["电视", "冰箱", "洗衣机", "空调", "热水器", "床", "暖气", "宽带", "天然气"]
for i in range (0,9):
    household_num.append(0)
for dict in sum_dict:
    for i in range(0,9):
        if dict[household[i]]==1:
            household_num[i]+=1

#日期-房价散点图
scatter=[]

for dict in sum_dict:
    date=date_change(dict["上架时间"])
    if date>20180000:
        if date<20190000:
            date=date-20180000
            day=date%100
            month=(date%10000-day)/100
            num=day+(month-1)*30
            price=dict["每平米房价"]
            scatter.append((num,price))
        else :
            date=date-20190000
            day = date % 100
            month = (date % 10000 - day) / 100
            num = day + (month-1) * 30+365
            price = dict["每平米房价"]
            scatter.append((num, price))

#用线性回归模型预测汉阳区未来房价
sklearn_datenum=[]
sklearn_price=[]
area=[]
for dict in hanyang_dict:
    date=date_change(dict["上架时间"])
    if date>20180000:
        if date<20190000:
            date=date-20180000
            day=date%100
            month=(date%10000-day)/100
            num=day+(month-1)*30
            sklearn_datenum.append([-1,num])
            sklearn_price.append(int(dict["每平米房价"]))
        else :
            date=date-20190000
            day = date % 100
            month = (date % 10000 - day) / 100
            num = day + (month-1) * 30+365
            sklearn_datenum.append([-1, num])
            sklearn_price.append(int(dict["每平米房价"]))
clf = LinearDiscriminantAnalysis()
clf.fit(sklearn_datenum, sklearn_price)
LinearDiscriminantAnalysis(n_components=None, priors=None, shrinkage=None, solver='svd',
                           store_covariance=False, tol=0.0001)
#预测从2018年1月1日开始的516天，即2019年6月1日到后面6个月,即到2019年12月1日的房价变化
for i in range(516,516+30*6):
    print(clf.predict([[-1, i]]))
#本部分将不做可视化处理（结果较前几个月微弱上涨，涨幅1-2元每平方米）





