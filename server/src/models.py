import os
import json
import pandas as pd
from . import data_keyword
from . import data_analyse
from . import pre_process

PATH_DATA_FOLDER = '../data/'
PATH_DATA_FILE_NETFLIX = 'data.csv'
PATH_DATA_FILE_DATASAURUS = 'countries.json'
PATH_DATA_POSITIVE_WORDS = 'positive_words.xlsx'
PATH_DATA_FEATURES = 'featuresdf.csv'


class Model:
    def __init__(self):
        self.DATA_FOLDER = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), PATH_DATA_FOLDER)

        try:
            self.data = pd.read_csv(os.path.join(
                self.DATA_FOLDER, PATH_DATA_FILE_NETFLIX))
        except:
            print(f'could not open: {PATH_DATA_FILE_NETFLIX}')

        try:
            with open(os.path.join(self.DATA_FOLDER, PATH_DATA_FILE_DATASAURUS), 'r', encoding='utf-8') as file:
                self.countries = json.load(file)
        except Exception as e:
            print(f'could not open: {PATH_DATA_FILE_DATASAURUS} because {e}')

        try:
            self.positive_word = pd.read_excel(os.path.join(
                self.DATA_FOLDER, PATH_DATA_POSITIVE_WORDS))
        except:
            print(f'could not open: {PATH_DATA_POSITIVE_WORDS}')

        try:
            self.df_feature = pd.read_csv(os.path.join(
                self.DATA_FOLDER, PATH_DATA_FEATURES))
        except:
            print(f'could not open: {PATH_DATA_FEATURES}')

    def get_keyword(self, region):
        data_keyword.data_keyword(self.data, region)
        return 'ok'

    def get_data(self):
        data_analyse.data_analyse(self.data)
        return 'ok'

    def pre_process(self):
        print(self.positive_word)
        pre_process.pre_process(self.data, self.positive_word, self.df_feature)
        return 'ok'

