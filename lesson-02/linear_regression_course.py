"""
Linear Regression: 实现了回归，其中包括线性函数的定义，为什么要用线性函数，loss的意义，梯度下降的意义，stochastic gradient descent
Use Boston house price dataset.
北京2020年房价的数据集，为什么我没有用北京房价的数据集呢？
Boston: room size, subway, highway, crime rate 有一个比较明显的关系，所以就观察关系比较容易
北京的房价：！远近，！房况 ==》 学区！！！！ => 非常贵 海淀区
"""
import random

from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


"""
为什么我没有一行一行解释代码
为什么我没有注释

==> 好的Python代码 一定是"自解释(self description)"
"""
dataset = load_boston()
data = dataset['data']
target = dataset['target']
columns = dataset['feature_names']

dataframe = pd.DataFrame(data)
dataframe.columns = columns
dataframe['price'] = target

# print(dataframe.corr()) # show the correlation of dataframe variables
# correlation => 如果一个值的增大，会引起另外一个值一定增大，而且是定比例增大 相关系数就越接近于1
# correlation => 0 就是两者之间没有任何关系
# correlation => -1 一个值增大 另外一个值一定减小 而且减小是成相等比例的

# sns.heatmap(dataframe.corr())
# plt.show()

# RM：小区平均的卧室个数
# LSTAT: 低收入人群在周围的比例

rm = dataframe['RM']
lstat = dataframe['LSTAT']
target = dataframe['price']


def model(x, w, b):
    # vectorized model
    return np.dot(x, w.T) + b


def loss(yhat, y):
    # numpy broadcast numpy广播方法
    return np.mean( (yhat - y) ** 2)


def partial_w(x, y, yhat):
    return np.array([2 * np.mean((yhat - y) * x[0]), 2 * np.mean((yhat - y) * x[1])])


def partial_b(x, y, yhat):
    return 2 * np.mean((yhat - y))


w = np.random.random_sample((1, 2)) # w normal
b = np.random.random() # 0 深度学习的时候会和大家详细解释
learning_rate = 1e-5
epoch = 200
losses = []

for i in range(epoch):
    batch_loss = []
    for batch in range(len(rm)):
        # batch training
        index = random.choice(range(len(rm)))
        rm_x, lstat_x = rm[index], lstat[index]
        x = np.array([rm_x, lstat_x])
        y = target[index]

        yhat = model(x, w, b)
        loss_v = loss(yhat, y)

        batch_loss.append(loss_v)

        w = w + -1 * partial_w(x, y, yhat) * learning_rate
        b = b + -1 * partial_b(x, y, yhat) * learning_rate

        if batch % 100 == 0:
            print('Epoch: {} Batch: {}, loss: {}'.format(i, batch, loss_v))
    losses.append(np.mean(batch_loss))

predicate = model(np.array([19, 7]), w, b)
print(predicate)


