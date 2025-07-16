from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('ad_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        tv = float(request.form['tv'])
        radio = float(request.form['radio'])
        newspaper = float(request.form['newspaper'])

        input_data = np.array([[tv, radio, newspaper]])
        prediction = model.predict(input_data)[0]
        output = round(prediction, 2)

        return render_template('index.html', prediction_text=f'📈 Predicted Sales: {output} units')
    except:
        return render_template('index.html', prediction_text="⚠️ Please enter valid numbers.")

if __name__ == '__main__':
    app.run(debug=True)
