from src.data_analyse import data_analyse
import pandas as pd
import os
import numpy as np
from src.data_keyword import data_keyword

if __name__ == '__main__':
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(CURRENT_DIR, 'data/data.csv')
    try:
        data = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        print('File not found')
        exit(1)
    data_analyse(data)
    data_keyword(data)

