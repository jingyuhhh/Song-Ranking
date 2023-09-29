import pandas as pd


def data_analyse(data: pd.DataFrame):
    pd.set_option('display.max_columns', None)
    print(data.head(100))


