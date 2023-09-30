import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.cm as cm
import json
from statsmodels.tsa.stattools import adfuller


def data_analyse(data: pd.DataFrame):
    # Top 10 tracks in the global throughout year 2017 with their total stream counts.
    top_tracks = data['Streams'].groupby(data['Track Name']).sum().sort_values(ascending=False)[:10]
    top_tracks = top_tracks.reset_index()
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    colormap = cm.get_cmap('Blues')
    norm = plt.Normalize(top_tracks['Streams'].min(), top_tracks['Streams'].max())
    top_tracks['Colors'] = top_tracks['Streams'].apply(lambda x: colormap(norm(x)))
    ax.barh(top_tracks['Track Name'], top_tracks['Streams'], color=top_tracks['Colors'])
    ax.invert_yaxis()
    ax.set_title('Top 10 tracks around the world', pad=20)
    ax.set_xlabel('Streams')
    plt.tight_layout()

    # Top 10 artists in the global throughout year 2017 with their total stream counts.
    top_artists = data['Streams'].groupby(data['Artist']).sum().sort_values(ascending=False)[:10]
    top_artists = top_artists.reset_index()
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    colormap = cm.get_cmap('Purples')
    norm = plt.Normalize(top_artists['Streams'].min(), top_artists['Streams'].max())
    top_artists['Colors'] = top_artists['Streams'].apply(lambda x: colormap(norm(x)))
    ax.barh(top_artists['Artist'], top_artists['Streams'], color=top_artists['Colors'])
    ax.invert_yaxis()
    ax.set_title('Top 10 artists around the world', pad=20)
    ax.set_xlabel('Streams')
    plt.tight_layout()

    # 由此可得知，全球最受欢迎的歌曲是Shape of You，最受欢迎的歌手是Ed Sheeran

    # Ranking changes of the Ed Sheeran's "Shape of You" alongside with the stream count changes
    shape_of_you = data[data['Track Name'] == 'Shape of You'].groupby('Date').sum()
    shape_of_you = shape_of_you.sort_values(by='Date')
    shape_of_you = shape_of_you.reset_index()
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    ax.plot(shape_of_you['Date'], shape_of_you['Streams'])
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    ax.set_title('Stream count changes of the Ed Sheeran\'s "Shape of You"', pad=20)
    ax.set_xlabel('Date')
    ax.set_ylabel('Streams')
    plt.tight_layout()

    # Rolling mean and standard deviation of the stream counts of the Ed Sheeran's "Shape of You"
    shape_of_you_streams = shape_of_you['Streams']
    roll_mean = pd.DataFrame.rolling(shape_of_you_streams, window=12).mean()
    roll_std = pd.DataFrame.rolling(shape_of_you_streams, window=12).std()
    plt.plot(shape_of_you_streams, color='blue', label='Original')
    plt.plot(roll_mean, color='red', label='mean')
    plt.plot(roll_std, color='black', label='std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    # plt.show()

    # ADF平稳性检验
    result = adfuller(shape_of_you_streams)
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    # ADF Statistic: -1.238973
    # p-value: 0.656610
    # p-value大于0.05
    shape_of_you_streams = shape_of_you_streams.diff().dropna()
    result = adfuller(shape_of_you_streams)
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    # ADF Statistic: -4.435676
    # p - value: 0.000257
    # p-value小于0.05，所以可以拒绝原假设，即该序列平稳



