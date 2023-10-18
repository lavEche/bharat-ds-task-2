from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name)

# Load the pre-trained model
with open('titanic_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user inputs
    pclass = int(request.form.get('pclass'))
    sex = request.form.get('sex')
    age = float(request.form.get('age'))
    
    # Preprocess the inputs (you may need more preprocessing)
    # Here, we'll perform one-hot encoding for 'sex' feature
    sex_male = 1 if sex.lower() == 'male' else 0
    sex_female = 1 if sex.lower() == 'female' else 0
    
    # Make a prediction using the model
    prediction = model.predict([[pclass, age, sex_male, sex_female]])
    
    # Interpret the prediction (1: Survived, 0: Did not survive)
    result = 'Survived' if prediction[0] == 1 else 'Did not survive'
    
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
