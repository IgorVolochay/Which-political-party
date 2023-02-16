import os
import json

import tensorflow as tf

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout

def json_load() -> (dict):
    if not "datasets" in os.getcwd():
        os.chdir("../datasets")
    
    try:
        with open("dataset.json", "r", encoding='utf8') as JSON:
            dataset = json.load(JSON)
    except:
        print(" ! \'dataset.json\' file is missing from: ~/Which-political-party/datasets")
        return

    return dataset

def markup_dataset(raw_data:dict) -> (tuple):
    x, y = list(), list()

    for data_output in raw_data.keys():
        for data_input in raw_data[data_output]:
            x.append(data_input)
            y.append(json.loads(data_output))

    return x, y

def neural_network(data_input:list, data_output:list) -> (None):
    os.chdir("../model")
    model = Sequential()

    model.add(Dense(units=256, input_shape=(len(data_input[0]),)))
    model.add(Dropout(0.2))
    model.add(Dense(units=256, input_shape=(256,), activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(units=5, input_shape=(256,)))
    model.compile(optimizer="adam", loss="mean_squared_error", metrics=['accuracy'])

    history = model.fit(data_input, data_output, epochs=200)

    model.evaluate(data_input, data_output)
    model.save("model versions/V0")

raw_data = json_load()
data_input, data_output = markup_dataset(raw_data)
neural_network(data_input, data_output)