# flask w/ model ML
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        body = request.json
        # 8 vars
        lt = body['LT Layer Thickness']
        as2_pressure = body['AS2 Pressure']
        gt = body['GT']
        at = body['AT']
        annealing_time = body['Annealing time']
        intended_thickness = body['Intended Thickness']
     
        # model prediction
        prediction = model.predict([[
            lt,as2_pressure,gt,at,annealing_time,intended_thickness
        ]])[0]
        return jsonify({
            prediction
        })
    elif request.method == 'GET':
        return jsonify({
            'status': 'Anda nge-GET'
        })
    else:
        return jsonify({
            'status': 'Anda tidak nge-POST & nge-GET'
        })

@app.route('/predictform', methods = ['POST', 'GET'])
def predictform():
    if request.method == 'POST':
        body = request.form
        lt = float(body['LT Layer Thickness'])
        as2_pressure = float(body['AS2 Pressure'])
        gt = float(body['GT'])
        at = float(body['AT'])
        annealing_time = float(body['Annealing time'])
        intended_thickness = float(body['Intended Thickness'] )       
        # model prediction
        result = model.predict([[
            lt,as2_pressure,gt,at,annealing_time,intended_thickness 
        ]])[0]
        return render_template('home.html', prediction_text='Predicted value of Roughness {}'.format(result))
        # return render_template('result.html', body=body)


if __name__ == '__main__':
    with open('saved_model.pkl', 'rb') as f:
        model = pickle.load(f)
    app.run(debug = True)