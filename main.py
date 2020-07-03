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
    return render_template('main.html')

@app.route("/form_pred", methods=["POST", "GET"])
def data_fetch():
    if request.method == "POST":
        year_dat = request.form["year"]
        enginehp_dat = request.form["enginehp"]
        enginecylinders_dat = request.form["enginecylinders"]
        transmissiontype_dat = request.form["transmissiontype"]
        fuel_dat = request.form["fuel"]
        cmpg_dat = request.form["cmpg"]
        hmpg_dat = request.form["hmpg"]
        make_dat = request.form["make"]
        mcategory_dat = request.form["mcategory"]
        drivenwheels_dat = request.form["drivenwheels"]
        return redirect(url_for("final", year = year_dat,enginehp = enginehp_dat, enginecylinders = enginecylinders_dat, transmissiontype = transmissiontype_dat, fuel = fuel_dat , \
                                 cmpg = cmpg_dat, hmpg = hmpg_dat, make = make_dat, mcategory = mcategory_dat, drivenwheels = drivenwheels_dat))  
    else:
        return render_template("form1.html") 

@app.route("/<year> /<enginehp> /<enginecylinders> /<transmissiontype> /<fuel> /<cmpg> /<hmpg> /<make> /<mcategory> /<drivenwheels>")
def final(year,enginehp,enginecylinders,transmissiontype,fuel,cmpg,hmpg,make,mcategory,drivenwheels):
    nm = [year,enginehp,enginecylinders,transmissiontype,fuel,cmpg,hmpg,make,mcategory,drivenwheels]
    lst = []
    for i in range(len(nm)):
        lst.append(nm[i])
        i = i+1
    a = get_predictions(lst)
    return render_template("form1.html")

@app.route('/pred')
def pred_page():
    a = get_predictions(lst)
    print(a)
    return render_template("form2.html", value = a)


if __name__ == "__main__":
    app.run()
