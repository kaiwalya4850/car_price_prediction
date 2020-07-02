from flask import Flask, render_template, request, redirect, url_for, session
from sklearn import model_selection
import pickle
import numpy as np

app = Flask(__name__)

# Loading saved model for predictions #
def get_predictions(list_of_ip):
    filename = 'saved_model.sav'
    model = pickle.load(open(filename, 'rb'))
    result = model.predict(np.array([list_of_ip]))
    result = np.expm1(result)
    result = result[0]
    result = round(result,3)
    return result

# Pass input like this and get predictions #
#lst = [335,2011,6,3,6,19,4,26,37,3]
#a = get_predictions(lst)
#print(a)

@app.route('/')
def homepage():
    return render_template('form1.html')

# @app.route("/pred_form", methods=["POST", "GET"])




if __name__ == "__main__":
    app.run()
