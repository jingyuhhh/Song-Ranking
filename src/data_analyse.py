import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.cm as cm
import json


def data_analyse(data: pd.DataFrame):
    # 1. Top 10 tracks in the global throughout year 2017 with their total stream counts.
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
    # plt.show()

    # 2. Top 10 artists in the global throughout year 2017 with their total stream counts.
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
    # plt.show()

    # 3. Top 10 tracks in each continent throughout year 2017 with their total stream counts.
    with open('data/countries.json', 'r', encoding='utf-8') as f:
        countries = json.load(f)
    continents = [countries[country]['continent'] for country in countries]
    continents = np.unique(continents)
    print(continents)
    # ['AF' 'AN' 'AS' 'EU' 'NA' 'OC' 'SA']
    continent_countries = {}
    for continent in continents:
        continent_countries[continent] = [country.lower() for country in countries
                                          if countries[country]['continent'] == continent]

    # 4. Ranking changes of the Ed Sheeran's "Shape of You" alongside with the stream count changes
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
    plt.show()
