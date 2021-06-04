from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server

import pickle
import numpy as np
model = pickle.load(open('flight_predict.pkl', 'rb'))
app = Flask(__name__)

def predict():
    vector_id = input('Vetor_id(either 1 or2)',type=NUMBER)
    pickup_longitude = input('pickup_logitude(it is neagtive number)',type=FLOAT)
    dropoff_longitude = input('dropoff_logitude(it is negative number)',type=FLOAT)
    pickup_latitude = input('pickup_latitude',type=FLOAT)
    dropoff_latitude = input('dropoff_latitude',type=FLOAT)
    pickup_month = input('pick_up month from 1 to 12',type=NUMBER)
    pickup_day = input('pickup day from 1 to 31',type=NUMBER)
    pickup_hour  = input('pickup hour from 1 to 24',type=NUMBER)
    pickup_min  = input('pickup min from 1 to 60',type=NUMBER)
    pickup_sec  = input('pickup secfrom 1 to 60',type=NUMBER)
    dropoff_month = input('dropoff month from 1 to 12',type=NUMBER)
    dropoff_day  = input('dropoff day from 1 to 31',type=NUMBER)
    dropoff_hour = input('dropoff hour from 1 to 24',type=NUMBER)
    dropoff_min  = input('dropoff min from 1 to 60',type=NUMBER)
    dropoff_sec  = input('dropoff secfrom 1 to 60',type=NUMBER)
    
    prediction = model.predict([[vector_id,pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude,pickup_month,pickup_day,pickup_hour,pickup_min,pickup_sec,dropoff_month,dropoff_day,dropoff_hour,dropoff_min,dropoff_sec]])
    output = prediction 
    if output <= 0:
        put_text('Wrong values u submit')
    else:    
        put_text('Trip_Duration :',output)
    
app.add_url_rule('/tool', 'webio_view', webio_view(predict),
            methods=['GET', 'POST', 'OPTIONS'])
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(predict, port=args.port)