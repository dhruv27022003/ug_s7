import pickle
import json
import numpy as np

__data_columns = None
__model = None

def get_estimated_quality(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity):
    try:
        loc_index = __data_columns.index()
    except:
        loc_index = -1
    print("Data recieved") 
    x = np.zeros(len(__data_columns))
    x[0] = ph
    x[1] = hardness
    x[2] = solids
    x[3] = chloramines
    x[4] =  sulfate
    x[5] =  conductivity
    x[6] =  organic_carbon
    x[7] =  trihalomethanes
    x[8] =  turbidity

    if loc_index>=0:
        x[loc_index] = 1
    X_input = np.array([1,2,3,4,5,6,7,8,9])
    c = __model.predict(X_input.reshape(1,-1))
    print(c[0])
    print(type(c));

    print("yooo2")
    
    return c[0]


def load_saved_artifacts():
    print("loading saved artifacts...start1")
    global  __data_columns
    with open("./columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
    global __model
    if __model is None:
       with open('./waterQuality.pickle', 'rb') as f:
          __model = pickle.load(f)
    print("loading saved artifacts...done")



