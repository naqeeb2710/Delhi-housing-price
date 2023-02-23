import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    result=__model.predict([x])/100000
    return round(result[0],2)

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open('columns.json', "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('Delhi_house_price.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_location_names())
    print(get_estimated_price('Lajpat Nagar', 1000, 4, 4))
    print(get_estimated_price('Lajpat Nagar', 1000, 5, 4))
    print(get_estimated_price('Lajpat Nagar', 1000, 2, 2))