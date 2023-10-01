import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import pandas as pd
import csv


def data_keyword(data: pd.DataFrame):

    # 读取Track Name列名
    key = data[data['Region'] == 'us']
    key = key['Track Name']

    # 创建txt，删除索引和列名
    key.to_csv('keywords.txt', index=False, header=False)

    # 读取刚刚保存的txt
    with open("keywords.txt", "r", encoding='gbk', errors='ignore') as f:
        text = f.read()
    f.close()
    # 这些可有可无，主要是分割
    cut = jieba.cut(text)
    text = ' '.join(cut)

    # 创建词云图，很简单
    wc = WordCloud(
        background_color="white",
        repeat=True,
        font_path='msyh.ttc',
    )
    wc.generate(text)
    plt.axis("off")
    plt.imshow(wc, interpolation="bilinear")
    plt.show()
    # 打开方式是以一个窗口弹出，可以改成直接保存
