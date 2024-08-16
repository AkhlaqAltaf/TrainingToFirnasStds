from flask import Flask, request, render_template, redirect, jsonify
from flask_cors import CORS
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)

# Hardcoded user database
database = {'safi': '123', 'james': 'aac', 'akhlaq': 'asdsf'}

@app.route('/')
def hello_world():
    return render_template("predictions.html")

@app.route('/form_login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return redirect("https://finance.yahoo.com/quote/BTC-USD/")
    else:
        name1 = request.form['username']
        pwd = request.form['password']

        if name1 not in database:
            return render_template('login.html', info='Invalid User')
        elif database[name1] != pwd:
            return render_template('login.html', info='Invalid Password')
        else:
            return render_template('home.html', name=name1)

@app.route('/find_data_minutes', methods=['POST'])
def find_data_minutes():
    if request.method == 'POST':
        # accessing json data from request
        data = request.get_json()
        w = [4.49861594e-03, 4.49954629e-03, -4.91822250e-06]
        b = 0.006013192981667382
        
        low = float(data.get('low'))
        open_ = float(data.get('open'))
        vol = float(data.get('vol'))

        # Linear combination
        y = low * w[0] + open_ * w[1] + vol * w[2] + b
        
        context = {'message': y}
        return jsonify(context)
    else:
        return "POST DATA"

@app.route('/find_data_daily', methods=['POST'])
@app.route('/find_data_daily', methods=['POST'])
@app.route('/find_data_daily', methods=['POST'])
def find_data_daily():
    if request.method == 'POST':
        # Accessing json data from request
        data = request.get_json()
        w = [11716.56232343, -5173.3898968  , 6553.07205736 , 6553.07205736 ,120.91029698]
        b =  17815.393747051043
        
        # Extract and prepare the input data
        x = np.array([
            (float(data.get('open'))-1.741912e+04)/1.929588e+04,
            (float(data.get('low'))-1.699393e+04)/1.881681e+04,
            (float(data.get('close'))-1.743467e+04)/1.930544e+04,
            (float(data.get('adj'))-1.743467e+04)/1.930544e+04,
            (float(data.get('vol'))-1.751004e+10)/1.921570e+10
            ]).reshape(1, -1)

        # Standardize x
        print(x)
        
        # Linear combination with standardized inputs
        y_standardized = np.dot(x, w) + b

        # Manually reverse the standardization for the prediction
        y_original = y_standardized * 1.973042e+04 + 1.781639e+04
        
        # Convert the NumPy array to a Python float
        y_original = y_original.item()

        context = {'message': y_original}  # Prepare the response
        return jsonify(context)
    else:
        return "POST DATA"



if __name__ == '__main__':
    app.run(debug=True)
