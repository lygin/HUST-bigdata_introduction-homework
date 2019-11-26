# -*-coding:utf-8-*-
import json
ave_prices=[]
deal_num=[]
filename = '武汉东西湖区.json'
prices=[]
price1=[]
price2=[]
sum_dict=[]
with open(filename,encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
       dict=eval(data[1])
       sum_dict.append(dict)
       if dict["地铁便利性"] == 1:
            price1.append(dict["每平米房价"])
       else:
            price2.append(dict["每平米房价"])
       prices.append(dict["每平米房价"])
ave_prices.append(sum(prices)/len(prices))
deal_num.append(len(prices))

filename = '武汉新洲区.json'
prices=[]
with open(filename,encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
       dict=eval(data[1])
       sum_dict.append(dict)
       if dict["地铁便利性"] == 1:
            price1.append(dict["每平米房价"])
       else:
            price2.append(dict["每平米房价"])
       prices.append(dict["每平米房价"])
ave_prices.append(sum(prices)/len(prices))
deal_num.append(len(prices))

filename = '武汉江岸区.json'
prices=[]
with open(filename,encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
       dict=eval(data[1])
       sum_dict.append(dict)
       if dict["地铁便利性"] == 1:
            price1.append(dict["每平米房价"])
       else:
            price2.append(dict["每平米房价"])
       prices.append(dict["每平米房价"])
ave_prices.append(sum(prices)/len(prices))
deal_num.append(len(prices))

filename = '武汉江汉区.json'
prices=[]
with open(filename,encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
       dict=eval(data[1])
       sum_dict.append(dict)
       if dict["地铁便利性"] == 1:
            price1.append(dict["每平米房价"])
       else:
            price2.append(dict["每平米房价"])
       prices.append(dict["每平米房价"])
ave_prices.append(sum(prices)/len(prices))
deal_num.append(len(prices))

filename = '武汉蔡甸区.json'
prices=[]
with open(filename,encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
       dict=eval(data[1])
       sum_dict.append(dict)
       if dict["地铁便利性"] == 1:
            price1.append(dict["每平米房价"])
       else:
            price2.append(dict["每平米房价"])
       prices.append(dict["每平米房价"])
ave_prices.append(sum(prices)/len(prices))
deal_num.append(len(prices))

filename = '武汉青山区.json'
prices=[]
with open(filename,encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
       dict=eval(data[1])
       sum_dict.append(dict)
       if dict["地铁便利性"] == 1:
            price1.append(dict["每平米房价"])
       else:
            price2.append(dict["每平米房价"])
       prices.append(dict["每平米房价"])
ave_prices.append(sum(prices)/len(prices))
deal_num.append(len(prices))

#区合并处理：
jiekouprice=[]
filename ='武汉硚口区part1.json'
with open(filename,encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
       dict=eval(data[1])
       sum_dict.append(dict)
       jiekouprice.append(dict["每平米房价"])

filename ='武汉硚口区part2.json'
with open(filename,encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
       dict=eval(data[1])
       sum_dict.append(dict)
       jiekouprice.append(dict["每平米房价"])

filename ='武汉硚口区part3.json'
with open(filename,encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
       dict=eval(data[1])
       sum_dict.append(dict)
       jiekouprice.append(dict["每平米房价"])

filename ='武汉硚口区part4.json'
with open(filename,encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
       dict=eval(data[1])
       sum_dict.append(dict)
       jiekouprice.append(dict["每平米房价"])

filename ='武汉硚口区part5.json'
with open(filename,encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
       dict=eval(data[1])
       sum_dict.append(dict)
       jiekouprice.append(dict["每平米房价"])

filename ='武汉硚口区part6.json'
with open(filename,encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
       dict=eval(data[1])
       sum_dict.append(dict)
       jiekouprice.append(dict["每平米房价"])
deal_num.append(len(jiekouprice))
ave_prices.append(sum(jiekouprice)/len(jiekouprice))

hanyangprice = []
hanyang_dict=[]
filename = '武汉汉阳区part1.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        hanyang_dict.append(dict)
        sum_dict.append(dict)
        hanyangprice.append(dict["每平米房价"])

filename = '武汉汉阳区part2.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        hanyang_dict.append(dict)
        sum_dict.append(dict)
        hanyangprice.append(dict["每平米房价"])

filename = '武汉汉阳区part3.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        sum_dict.append(dict)
        hanyang_dict.append(dict)
        hanyangprice.append(dict["每平米房价"])

filename = '武汉汉阳区part4.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        sum_dict.append(dict)
        hanyang_dict.append(dict)
        hanyangprice.append(dict["每平米房价"])

filename = '武汉汉阳区part5.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        sum_dict.append(dict)
        hanyang_dict.append(dict)
        hanyangprice.append(dict["每平米房价"])
deal_num.append(len(hanyangprice))
ave_prices.append(sum(hanyangprice) / len(hanyangprice))

jiangxiaprice=[]
filename='武汉江夏区part1.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        sum_dict.append(dict)
        jiangxiaprice.append(dict["每平米房价"])

filename='武汉江夏区part2.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        sum_dict.append(dict)
        jiangxiaprice.append(dict["每平米房价"])

deal_num.append(len(jiangxiaprice))
ave_prices.append(sum(jiangxiaprice) / len(jiangxiaprice))

huangpoprice=[]
filename='武汉黄陂区part1.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        sum_dict.append(dict)
        huangpoprice.append(dict["每平米房价"])

filename='武汉黄陂区part2.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        sum_dict.append(dict)
        huangpoprice.append(dict["每平米房价"])

filename='武汉黄陂区part3.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        sum_dict.append(dict)
        huangpoprice.append(dict["每平米房价"])
deal_num.append(len(huangpoprice))
ave_prices.append(sum(huangpoprice) / len(huangpoprice))

wuchangprice=[]
filename='武汉武昌区part1.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        sum_dict.append(dict)
        wuchangprice.append(dict["每平米房价"])

filename='武汉武昌区part2.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        sum_dict.append(dict)
        wuchangprice.append(dict["每平米房价"])

filename='武汉武昌区part3.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        sum_dict.append(dict)
        wuchangprice.append(dict["每平米房价"])

filename='武汉武昌区part4.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        sum_dict.append(dict)
        wuchangprice.append(dict["每平米房价"])
deal_num.append(len(wuchangprice))
ave_prices.append(sum(wuchangprice) / len(wuchangprice))

hongshanprice=[]
filename='武汉洪山区part1.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        sum_dict.append(dict)
        hongshanprice.append(dict["每平米房价"])

filename='武汉洪山区part2.json'
with open(filename, encoding='utf-8') as f:
    datas = json.load(f)
    for data in datas:
        dict = eval(data[1])
        sum_dict.append(dict)
        hongshanprice.append(dict["每平米房价"])
deal_num.append(len(hongshanprice))
ave_prices.append(sum(hongshanprice) / len(hongshanprice))



subway_price=[sum(price1)/len(price1),sum(price2)/len(price2)]




