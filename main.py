from src.data_analyse import data_analyse
from src.pre_process import pre_process
import pandas as pd
import os
import numpy as np


if __name__ == '__main__':
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(CURRENT_DIR, 'data/data.csv')
    try:
        data = pd.read_csv(DATA_PATH)
        positive_word = pd.read_excel('data/positive_words.xlsx')
        df_feature = pd.read_csv("data/featuresdf.csv")
    except FileNotFoundError:
        print('File not found')
        exit(1)
    pre_process(data, positive_word, df_feature)
    data_analyse(data)

