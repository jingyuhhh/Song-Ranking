import os
import json
import pandas as pd
from . import data_keyword
from . import data_analyse

PATH_DATA_FOLDER = '../data/'
PATH_DATA_FILE_NETFLIX = 'data.csv'
PATH_DATA_FILE_DATASAURUS = 'countries.json'


class Model:
    def __init__(self):
        self.DATA_FOLDER = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), PATH_DATA_FOLDER)

        try:
            self.data = pd.read_csv(os.path.join(
                self.DATA_FOLDER, PATH_DATA_FILE_NETFLIX))
        except:
            print(f'could not open: {PATH_DATA_FILE_NETFLIX}')

        # load the datasaurus dataset
        try:
            with open(os.path.join(self.DATA_FOLDER, PATH_DATA_FILE_DATASAURUS), 'r', encoding='utf-8') as file:
                self.countries = json.load(file)
        except Exception as e:
            print(f'could not open: {PATH_DATA_FILE_DATASAURUS} because {e}')

    def get_keyword(self):
        data_keyword.data_keyword(self.data)
        return 'ok'

    def get_data(self):
        data_analyse.data_analyse(self.data, self.countries)
        return 'ok'

