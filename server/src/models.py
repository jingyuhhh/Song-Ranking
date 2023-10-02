import os
import json
import pandas as pd
from . import data_keyword
from . import data_analyse
# from . import data_forecast

PATH_DATA_FOLDER = '../data/'
PATH_DATA_FILE = 'data.csv'
PATH_DATA_FILE_FORECAST = 'feature_2017.csv'
PATH_DATA_FILE_DATASAURUS = 'countries.json'


class Model:
    def __init__(self):
        self.DATA_FOLDER = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), PATH_DATA_FOLDER)

        try:
            self.data = pd.read_csv(os.path.join(
                self.DATA_FOLDER, PATH_DATA_FILE))
        except:
            print(f'could not open: {PATH_DATA_FILE}')

        # load the datasaurus dataset
        try:
            with open(os.path.join(self.DATA_FOLDER, PATH_DATA_FILE_DATASAURUS), 'r', encoding='utf-8') as file:
                self.countries = json.load(file)
        except Exception as e:
            print(f'could not open: {PATH_DATA_FILE_DATASAURUS} because {e}')

        try:
            self.data_forecast = pd.read_csv(os.path.join(
                self.DATA_FOLDER, PATH_DATA_FILE_FORECAST))
        except:
            print(f'could not open: {PATH_DATA_FILE_FORECAST}')

    def get_keyword(self, region):
        data_keyword.data_keyword(self.data, region)
        return 'ok'

    def get_data(self):
        data_analyse.data_analyse(self.data, self.countries)
        return 'ok'

    # def predict(self):
        # data_forecast.data_forecast(self.data, self.data_forecast)
        # return 'ok'


