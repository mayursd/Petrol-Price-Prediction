import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask ( __name__ )
model = pickle.load ( open ( 'Pricemodel.model', 'rb' ) )


@app.route ( '/' )
def home() :
    return render_template ( 'index.html' )


@app.route ( '/predict', methods=[ 'POST' ] )
def predict() :
    '''
    For rendering results on HTML GUI
    '''
    int_features = [ int ( x ) for x in request.form.values ( ) ]
    print(int_features)
    prediction = model.predict ( [int_features] )

    output = ( prediction )

    return render_template ( 'index.html', prediction_text='Petrol Price should be $ {}'.format ( output ) )


if __name__ == "__main__" :
    app.run ( )
