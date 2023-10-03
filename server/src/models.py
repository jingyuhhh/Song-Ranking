import os
import json
import pandas as pd
from . import data_keyword
from . import data_analyse
# from . import data_forecast
from . import pre_process

PATH_DATA_FOLDER = '../data/'
PATH_DATA_FILE = 'data.csv'
PATH_DATA_FILE_FEATURE = 'featuresdf.csv'
PATH_DATA_FILE_DATASAURUS = 'countries.json'
PATH_DATA__FILE_POSITIVE_WORDS = 'positive_words.xlsx'


class Model:
    def __init__(self):
        self.DATA_FOLDER = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), PATH_DATA_FOLDER)

        try:
            self.data = pd.read_csv(os.path.join(
                self.DATA_FOLDER, PATH_DATA_FILE))
        except:
            print(f'could not open: {PATH_DATA_FILE}')

        try:
            self.positive_words = pd.read_excel(os.path.join(
                self.DATA_FOLDER, PATH_DATA__FILE_POSITIVE_WORDS))
        except:
            print(f'could not open: {PATH_DATA__FILE_POSITIVE_WORDS}')

        try:
            with open(os.path.join(self.DATA_FOLDER, PATH_DATA_FILE_DATASAURUS), 'r', encoding='utf-8') as file:
                self.countries = json.load(file)
        except Exception as e:
            print(f'could not open: {PATH_DATA_FILE_DATASAURUS} because {e}')


        try:
            self.data_feature = pd.read_csv(os.path.join(
                self.DATA_FOLDER, PATH_DATA_FILE_FEATURE))
        except:
            print(f'could not open: {PATH_DATA_FILE_FEATURE}')

    def get_keyword(self, region):
        data_keyword.data_keyword(self.data, region)
        return 'ok'

    def get_data(self):
        data_analyse.data_analyse(self.data, self.countries)
        return 'ok'

    # def predict(self):
    #     data_forecast.data_forecast(self.data, self.data_feature)
    #     return 'ok'

    def pre_process(self):
        pre_process.pre_process(self.data, self.positive_words, self.data_feature)
        return 'ok'


