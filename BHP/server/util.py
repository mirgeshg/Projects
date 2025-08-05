import json
import pickle
import numpy as np



__locations= None
__data_columns = None
__model= None


def get_estimated_price(location,sqft,bhk,bath):# in ".index" method there is a problem if it didin't find it it will throw an error
    #so we use try and catch
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index= -1

    x = np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index] =1#out of so many columns we are finding out the appropriate by making dummy and setting all the other var. as zero


    return __model.predict([x])[0]
    loc_index = np.where(X.columns==location)[0][0]
def get_location_names():
    return __locations
def load_saved_artifacts():
    print("load")
    global  __data_columns
    global  __locations

    with open("./artifacts/columns.json",'r') as f:  #r for as we are only reading the file
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("./artifacts/banglore_home_prices_model.pickle",'rb') as f:#as this is a binary model so we use rb
        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ =='__main__':
    load_saved_artifacts()

    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar ',1000,3,3))
    print(get_estimated_price('Kalhalli',1000,2,2))
    print(get_estimated_price('Eijpura', 1000,2,2))