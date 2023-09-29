import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.cm as cm


def data_analyse(data: pd.DataFrame):
    pd.set_option('display.max_columns', None)
    top_chart = data.loc[data['Position'] == 1, 'Artist'].value_counts().reset_index()
    top_chart.columns = ['Artist', 'top1_cnt']
    top_chart = top_chart.sort_values('top1_cnt', ascending=False)
    colormap = cm.get_cmap('Blues')
    norm = plt.Normalize(top_chart['top1_cnt'].min(), top_chart['top1_cnt'].max())
    top_chart['color'] = top_chart['top1_cnt'].apply(lambda x: colormap(norm(x)))
    fig, ax = plt.subplots()
    y_pos = np.arange(10)  # Return evenly spaced values within a given interval.
    ax.barh(top_chart['Artist'][:10], top_chart['top1_cnt'][:10], color=top_chart['color'][:10])
    ax.set_yticks(y_pos, labels=top_chart['Artist'][:10])
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Top 1 Number')
    ax.set_title('Best 10 Singer on Top 1 Number')

    plt.show()

