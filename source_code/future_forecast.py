from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib as plt
from 数据分析处理 import  price,area
linear = LinearRegression()
area = np.array(area).reshape(-1,1)
price = np.array(price).reshape(-1,1)
# 训练模型
model = linear.fit(area,price)
# 打印截距和回归系数
print(model.intercept_, model.coef_)

# 线性回归可视化(数据拟合)
linear_p = model.predict(area)
plt.figure(figsize=(12,6))
plt.scatter(area,price)
plt.plot(area,linear_p,'red')
plt.xlabel("area")
plt.ylabel("price")
plt.show()

# 使用train_test_split进行交叉验证
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=12)
print(x_train.shape,y_train.shape)
print(x_test.shape,y_test.shape)

# 模型训练
linear = LinearRegression()
model = linear.fit(x_train,y_train)
print(model.intercept_, model.coef_)

# 模型性能评分
price_end = model.predict(x_test)
score = model.score(x_test,y_test)
print("模型得分：",score)# 一般模型在0.6以上就表现的不错