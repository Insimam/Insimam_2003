from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('Data_model_pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    age = request.form['a']
    rbc = request.form['b']
    bgr = request.form['c']
    serum = request.form['d']
    HB = request.form['e']
    rc = request.form['f']
    cad = request.form['g']
    arr = np.array([[age, rbc, bgr, serum, HB, rc, cad]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)