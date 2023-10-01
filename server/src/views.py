from . import app
from .models import Model
from flask import request
import json

# initialize the model
model = Model()
print("================================================================")


@app.route('/get')
def _get():
    return "Get"


@app.route('/get_keyword', methods=['POST'])
def get_keyword():
    data = request.json
    region = data['country']
    return model.get_keyword(region)


@app.route('/get_data', methods=['POST'])
def get_data():
    return model.get_data()

