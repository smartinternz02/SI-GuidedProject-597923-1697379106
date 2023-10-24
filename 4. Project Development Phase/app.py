from flask import Flask
from flask import render_template
from flask import request
import pickle

app = Flask(__name__)
model = pickle.load(open('', 'rb'))

@app.route('/')
def start():
    return render_template('/webapp/index.html')

@app.route('/login', methods=['POST'])
def login():
    attr1 = float(request.form["attr1"])



if __name__ == '__main__':
    app.run(debug=True)