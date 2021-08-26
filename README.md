# Boston_Housing_Price_Prediction_API

A simple API endpoint tha predicts boston house prices based on "inputs" passed in the post request.

# Usage
The API can be found on https://bosnprice.herokuapp.com and has one endpoint where data can be posted to :https://bosnprice.herokuapp.com/predict

The input is a list containing 13 parameters and this is how the code should be inputed in the end point to print out the predicted price in a list.

import requests
import json


resp = requests.post("https://bosnprice.herokuapp.com/predict", 
                     data=json.dumps({"inputs": [[6.320e-03,
            1.800e+01,
            2.310e+00,
            0.000e+00,
            5.380e-01,
            6.575e+00,
            6.520e+01,
            4.090e+00,
            1.000e+00,
            2.960e+02,
            1530e+01,
            3.969e+02,
            5.980e+00
            ],
            [0.02731,
             0.00,
             7.07,
             0.00,
             0.469,
             6.421,
             78.9,
             4.9671,
             2.00,
             242,
             17.8,
             396.9,
             9.14
             ]]
            }))
print(resp.text)

And Output should be the form of: 
{"predicted_price": [22.773209661537333, 21.271482619210875]}
