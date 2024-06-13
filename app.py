from flask import Flask, request
import joblib
import numpy
import sklearn

MODEL_PATH = 'mlmodels/model.pkl'
SCALER_X_PATH = 'mlmodels/scaler_x.pkl'
SCALER_Y_PATH = 'mlmodels/scaler_y.pkl'

app = Flask(__name__)
model = joblib.load(MODEL_PATH)
sc_x = joblib.load(SCALER_X_PATH)
sc_y = joblib.load(SCALER_Y_PATH)

@app.route('/predict_price', methods=['GET'])
def predict():
    args = request.args
    required_params = ['floor', 'rooms', 'studio', 'area', 'renovation']
    
    # Check for missing required parameters
    for param in required_params:
        if param not in args:
            return f'Missing required parameter: {param}', 500

    try:
        floor = int(args.get('floor'))
        rooms = int(args.get('rooms'))
        studio = args.get('studio').lower()
        if studio not in ['true', 'false']:
            return 'Invalid value for studio, must be true or false', 500
        # Convert 'true'/'false' to boolean
        studio = studio == 'true'
        area = float(args.get('area'))
        renovation = int(args.get('renovation'))
    except ValueError:
        return 'Invalid parameter type', 500

    # Create the input array for the model
    x = numpy.array([floor, rooms, studio, area, renovation]).reshape(1, -1)
    x = sc_x.transform(x)

    # Make the prediction
    result = model.predict(x)
    result = sc_y.inverse_transform(result.reshape(1, -1))

    return str(result[0][0])

if __name__ == '__main__':
    app.run(debug=True, port=5444, host='0.0.0.0')