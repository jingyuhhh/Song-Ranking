import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.cm as cm
import json
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

ASSETS_PATH = '../client/src/assets'


def data_analyse(data: pd.DataFrame, countries: dict):
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
    fig.savefig(ASSETS_PATH + '/top_10_tracks.png')

    # Top 10 artists in the global throughout year 2017 with their total stream counts.
    top_artists = data['Streams'].groupby(data['Artist']).sum().sort_values(ascending=False)[:10]
    top_artists = top_artists.reset_index()
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    colormap = cm.get_cmap('Blues')
    norm = plt.Normalize(top_artists['Streams'].min(), top_artists['Streams'].max())
    top_artists['Colors'] = top_artists['Streams'].apply(lambda x: colormap(norm(x)))
    ax.barh(top_artists['Artist'], top_artists['Streams'], color=top_artists['Colors'])
    ax.invert_yaxis()
    ax.set_title('Top 10 artists around the world', pad=20)
    ax.set_xlabel('Streams')
    plt.tight_layout()
    fig.savefig(ASSETS_PATH + '/top_10_artists.png')

    # top 10 tracks for each continent
    continents = {}
    for name, country in countries.items():
        continent = country['continent']
        if continent not in continents:
            continents[continent] = []
        continents[continent].append(name.lower())

    print(continents.keys())
    # 'EU', 'AS', 'NA', 'AF', 'AN', 'SA', 'OC'

    def get_top_songs_by_continent(region):
        top_songs = (
            data[data['Region'].isin(continents[region])]
            ['Streams']
            .groupby(data['Track Name'])
            .sum()
            .sort_values(ascending=False)[:10]
            .reset_index()
        )
        return top_songs

    eu = get_top_songs_by_continent('EU')
    as_ = get_top_songs_by_continent('AS')
    na = get_top_songs_by_continent('NA')
    sa = get_top_songs_by_continent('SA')
    oc = get_top_songs_by_continent('OC')

    def draw_barh(top_songs, title, color='Blues'):
        fig, ax = plt.subplots()
        fig.set_size_inches(10, 6)
        colormap = cm.get_cmap(color)
        norm = plt.Normalize(top_songs['Streams'].min(), top_songs['Streams'].max())
        top_songs['Colors'] = top_songs['Streams'].apply(lambda x: colormap(norm(x)))
        ax.barh(top_songs['Track Name'], top_songs['Streams'], color=top_songs['Colors'])
        ax.invert_yaxis()
        ax.set_title(title, pad=20)
        ax.set_xlabel('Streams')
        plt.tight_layout()
        fig.savefig(ASSETS_PATH + '/top_10_tracks_in_{}.png'.format(title.split()[-1].lower()))

    draw_barh(eu, 'Top 10 tracks in December 2017 for Europe', 'Reds')
    draw_barh(as_, 'Top 10 tracks in December 2017 for Asia', 'Greens')
    draw_barh(na, 'Top 10 tracks in December 2017 for NA', 'Purples')
    draw_barh(sa, 'Top 10 tracks in December 2017 for SA', 'Oranges')
    draw_barh(oc, 'Top 10 tracks in December 2017 for Oceania', 'Blues')

    # top 10 artists for each continent
    def get_top_artists_by_continent(region):
        top_artists = (
            data[data['Region'].isin(continents[region])]
            ['Streams']
            .groupby(data['Artist'])
            .sum()
            .sort_values(ascending=False)[:10]
            .reset_index()
        )
        return top_artists

    eu = get_top_artists_by_continent('EU')
    as_ = get_top_artists_by_continent('AS')
    na = get_top_artists_by_continent('NA')
    sa = get_top_artists_by_continent('SA')
    oc = get_top_artists_by_continent('OC')

    def draw_barh(top_artists, title, color='Blues'):
        fig, ax = plt.subplots()
        fig.set_size_inches(10, 6)
        colormap = cm.get_cmap(color)
        norm = plt.Normalize(top_artists['Streams'].min(), top_artists['Streams'].max())
        top_artists['Colors'] = top_artists['Streams'].apply(lambda x: colormap(norm(x)))
        ax.barh(top_artists['Artist'], top_artists['Streams'], color=top_artists['Colors'])
        ax.invert_yaxis()
        ax.set_title(title, pad=20)
        ax.set_xlabel('Streams')
        plt.tight_layout()
        fig.savefig(ASSETS_PATH + '/top_10_artists_in_{}.png'.format(title.split()[-1].lower()))

    draw_barh(eu, 'Top 10 artists in December 2017 for Europe', 'Reds')
    draw_barh(as_, 'Top 10 artists in December 2017 for Asia', 'Greens')
    draw_barh(na, 'Top 10 artists in December 2017 for NA', 'Purples')
    draw_barh(sa, 'Top 10 artists in December 2017 for SA', 'Oranges')
    draw_barh(oc, 'Top 10 artists in December 2017 for Oceania', 'Blues')

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
    fig.savefig(ASSETS_PATH + '/stream_count_changes.png')

    # Rolling mean and standard deviation of the stream counts of the Ed Sheeran's "Shape of You"
    shape_of_you_streams = shape_of_you['Streams']
    roll_mean = pd.DataFrame.rolling(shape_of_you_streams, window=12).mean()
    roll_std = pd.DataFrame.rolling(shape_of_you_streams, window=12).std()
    plt.plot(shape_of_you_streams, color='blue', label='Original')
    plt.plot(roll_mean, color='red', label='mean')
    plt.plot(roll_std, color='black', label='std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    fig.savefig(ASSETS_PATH + '/rolling_mean_std.png')

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

    # 自相关图和偏相关图
    fig = plt.figure(figsize=(12, 8))
    ax1 = fig.add_subplot(211)
    fig = plot_acf(shape_of_you_streams, lags=20, ax=ax1, alpha=0.05)
    ax2 = fig.add_subplot(212)
    fig = plot_pacf(shape_of_you_streams, lags=20, ax=ax2, alpha=0.05)
    fig.savefig(ASSETS_PATH + '/acf_pacf.png')
    # 由自相关图和偏相关图可知，自相关图在滞后1阶后截尾，偏相关图在滞后1阶后截尾，所以可以使用ARMA(1,1)模型

