from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import pickle


app = Flask(__name__)
model = pickle.load(open('XGB_model.pkl', 'rb'))


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    # Getting the input values from the application
    attr1 = float(request.form["attr1"])
    attr2 = float(request.form["attr2"])
    attr3 = float(request.form["attr3"])
    attr4 = float(request.form["attr4"])
    attr5 = float(request.form["attr5"])
    attr6 = float(request.form["attr6"])
    attr7 = float(request.form["attr7"])
    attr8 = float(request.form["attr8"])
    attr9 = float(request.form["attr9"])
    attr10 = float(request.form["attr10"])

    # Making an input array for the model
    inputs = [[attr1, attr2, attr3, attr4, attr5, attr6, attr7, attr8, attr9, attr10]]

    # Getting the prediction
    prediction = model.predict(inputs)
    print(prediction)
    if prediction == 1:
        output = "!! THE COMPANY CAN GO BANKRUPT !!"
    else:
        output = "!! THE COMPANY IS SAFE !!"

    # Returning the prediction
    return jsonify({'y': output})


if __name__ == '__main__':
    app.run(debug=True)