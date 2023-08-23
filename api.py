from flask import Flask, request, jsonify
from utils import *

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return 'Welcome to MlForecast!'

@app.route('/prediction', methods=['POST'])
def prediction() -> Dict[str, List[float]]:
    model: str = request.json['model']
    data: List[float] = request.json['data']
    predict_length: int = request.json['predict_length']
    mlf = model_dict[model]
    prediction: List[float] = list(mlf.predict(predict_length)['Lasso'])
    prediction = [round(value, 2) for value in prediction]

    return jsonify({'prediction': prediction})

if __name__ == '__main__':

    model_dict = load_models('./model_pkl/')
    app.run(host='127.0.0.1', port=5000, debug=True)

