import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import torch
from pandas.plotting import autocorrelation_plot
from data_forecast import  data_forecast

from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

from sklearn.metrics import mean_squared_error as mse
pd.options.mode.chained_assignment = None
if __name__ == '__main__':
    data = pd.read_csv('./archive/data.csv') # 这里改成github中的路径
    song_feature = pd.read_csv('./archive/featuresdf.csv')# 这里就是读取两个测试集，然后就行了
    # 把路径更改一下还需要
    data_forecast(data,song_feature)

