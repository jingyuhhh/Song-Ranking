import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import torch
from pandas.plotting import autocorrelation_plot


from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

from sklearn.metrics import mean_squared_error as mse
pd.options.mode.chained_assignment = None

# data = pd.read_csv('./archive/data.csv')
# 在本地测试的时候更改的该部分

# 由于上面已经完成对于数据的分析和处理
# 知道模型选取的参数,AR 1 SMA(seasonal MA) 1
def data_forecast(data:pd.DataFrame,song_feature:pd.DataFrame):
    df_train = data
    df_train.dropna(inplace=True)
    df_train['Date'] = pd.to_datetime(df_train['Date'])

    df_us = df_train.loc[df_train.Region == 'us', :]
    shape_of_you = df_us[['Date', 'Streams']].loc[df_us['Track Name'] == 'Shape of You', :]
    shape_of_you.set_index('Date', inplace=True)

    # 参数:歌曲数据集合
    # 这个函数用于分化测试集和训练集
def get_X(song):
    nrows = song.shape[0]
    num_train = int(nrows * 0.8)
    X_train, X_test = song.iloc[np.arange(0, num_train), :], song.iloc[np.arange(num_train, nrows), :]
    return X_train, X_test, (nrows, num_train)

# 解释参数
# 模型,行列数据,训练集,表格名称,外部回归变量的处理,两个集合的划分比例
# 该函数用于训练模型
def mdl_shape(mdl, row_info, X_train, name='(1,1,0)x(1,1,0,7)xtrend n Model', exog=None, portion=0.5):
    nrows, num_train = row_info
    result = mdl.fit()

    forecast = result.predict(start=int(nrows * portion), end=num_train, dynamic=True, exog=exog)
    X_train['forecast'] = np.hstack([np.zeros((int(nrows * portion) - 1)), forecast.values])

    f, ax = plt.subplots(1, 1, figsize=(12, 4))

    # 指定 Streams 的颜色为蓝色，forecast 的颜色为红色
    X_train['Streams'].plot(ax=ax, color='blue', label='Streams')
    X_train['forecast'].plot(ax=ax, color='red', label='Forecast')

    ax.set_title(name)
    ax.legend()  # 添加图例，显示 Streams 和 Forecast 的标签
    plt.show()

# 解释参数
# 训练好的模型,行列数据,测试集,表格名称,外部回归变量
# 这个是
def prediction_mdl(mdl, row_info, X_test, name='', exog=None):
    nrows, num_train = row_info
    result = mdl.fit()

    forecast = result.predict(start=num_train - 1, end=nrows, dynamic=True, exog=exog)
    X_test['forecast'] = forecast[2:].values

    f, ax = plt.subplots(1, 1, figsize=(12, 4))

    # 指定 Streams 的颜色为蓝色，forecast 的颜色为红色
    X_test['Streams'].plot(ax=ax, color='green', label='Streams')
    X_test['forecast'].plot(ax=ax, color='m', label='Forecast')

    ax.set_title(name)
    ax.legend()  # 添加图例，显示 Streams 和 Forecast 的标签
    plt.show()

def tf_song_feature(song_feature):
    song_feature.drop(['id'], axis=1, inplace=True)
    song_feature.rename(columns={'name': 'Track Name', 'artists': 'Artist'}, inplace=True)
    return song_feature

    # 当前情况未知具体拟合情况,所以接下来进行几次模拟

    # 先注明,本处使用SARIMAX模型,对于模型中参数解释如下

    # order=(1,1,0): 这是 SARIMAX模型的非季节性部分的阶数。
    # 具体来说，(1,1,0) 表示模型中包含一个自回归（AR）项的阶数为 1，
    # 差分（I）项的阶数为 1，和移动平均（MA）项的阶数为 0。
    # 这些参数用于描述时间序列中的自相关和差分结构

    # seasonal_order=(0,1,1,7)
    # 这是 SARIMAX 模型的季节性部分的阶数。具体来说，(1,1,0,7)
    # 表示模型中包含一个季节性自回归（SAR）项的阶数为 1，
    # 季节性差分（SI）项的阶数为 1，季节性移动平均（SMA）项的阶数为 0，季节性周期为 7。
    # 这些参数用于描述时间序列中的季节性结构，其中季节周期为 7 表示数据每周重复。

    #  trend 这个参数用于指定趋势项的设置

    # y(t) = c + αt + βt ^ 2 + γt ^ 3 + ϵ(t)
    # y(t)是时间序列数据的观测值。
    # c 是常数项，表示时间序列数据的初始水平。
    # t 是时间的索引，表示观测值的顺序。
    # α是线性趋势项的系数，表示时间的线性变化对观测值的影响。
    # β是二次趋势项的系数，表示时间的二次变化对观测值的影响。
    # γ是三次趋势项的系数，表示时间的三次变化对观测值的影响。
    # ϵ(t) 是随机误差，表示未能被趋势项解释的随机波动。
data = pd.read_csv('./archive/data.csv')
df_train = data
df_train.dropna(inplace=True)
df_train['Date'] = pd.to_datetime(df_train['Date'])

df_us = df_train.loc[df_train.Region == 'us', :]
shape_of_you = df_us[['Date', 'Streams']].loc[df_us['Track Name'] == 'Shape of You', :]
shape_of_you.set_index('Date', inplace=True)
X_train, X_test, row_info = get_X(shape_of_you)
mdl1 = SARIMAX(X_train, trend='n', order=(1, 1, 0), seasonal_order=(0, 1, 1, 7))
mdl_shape(mdl1, row_info, X_train, name='AR = 1,I = 1,SMA = 1,Periods = 7,Trend = no')
# 显然效果没那么好,因为后序的趋势是下降的
# 所以接下来我们增加一个趋势

X_train, X_test, row_info = get_X(shape_of_you)
mdl2 = SARIMAX(X_train, trend=[1, 0, 0, 1], order=(1, 1, 0), seasonal_order=(0, 1, 1, 7))
mdl_shape(mdl2, row_info, X_train, name='AR = 1,I = 1,SMA = 1,Periods = 7,Trend = a+b*(x^3)')
# 这样看来,我们的训练模型的效果基本不错了
# 但是我们还要预测后面的数据,所以接下来是预测部分
prediction_mdl(mdl2, row_info, X_test, name='Prediction AR = 1,I = 1,SMA = 1,Periods = 7,Trend = a+b*(x^3)')
# 这个预测的效果非常糟糕,几乎没有拟合上,尤其到后面的时候,自己就往下掉了

# 当用a *X预测的时候,虽然prediction的效果很好
#  但是train中末端效果拟合并不是很好
X_train, X_test, row_info = get_X(shape_of_you)
mdl2 = SARIMAX(X_train, trend=[0, 1, 0, 0], order=(1, 1, 0), seasonal_order=(0, 1, 1, 7))
prediction_mdl(mdl2, row_info, X_test, name='AR = 1,I = 1,SMA = 1,Periods = 7,Trend = a')

# 接下来,我们通过动态调整x的过程来寻找到一个
# 两个效果都不错的x
# 从歌曲的特征入手
# TODO :应该是要更改文件路径的,当前这里使用的本地的路径
song_feature = pd.read_csv('./archive/featuresdf.csv')
# 对数据的预处理,去除不必要的行
song_feature = tf_song_feature(song_feature)
exog = song_feature.loc[0, :].values[2:]
exog = exog.astype(float)  # 转为浮点型
X_train, X_test, row_info = get_X(shape_of_you)

# 在加入外部回归变量之后,重新进行拟合
mdl2 = SARIMAX(endog=X_train, exog=np.array([exog for i in range(X_train.shape[0])]), trend=[0, 1, 0, 0],
               order=(1, 1, 0), seasonal_order=(0, 1, 1, 7))
mdl_shape(mdl2, row_info, X_train, name=' With Exog,AR = 1,I = 1,SMA = 1,Periods = 7,Trend = a * x',
          exog=exog.reshape(1, 13))
X_train, X_test, row_info = get_X(shape_of_you)
prediction_mdl(mdl2, row_info, X_test,
               name=' With Exog, Prediction AR = 1,I = 1,SMA = 1,Periods = 7,Trend = a * x At Test',
               exog=np.array([exog for i in range(75)]))
    # 显然本次的效果下,两个测试集都得到了很好的满足



