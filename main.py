from flask import Flask, render_template,request
import utilities.gender

app = Flask(__name__)


'#takes care of admin find names'
@app.route('/checkName', methods = ['GET', 'POST'])
def checkname():
    if request.method == 'POST':
        name = request.form['searchName']

        gender = utilities.gender.find_gender_with_db(name)
        if not gender:
            gender = utilities.gender.find_gender_with_api(name)

        return render_template("adminTrue.html", name = name, gender = gender)

    return render_template("adminLogin.html")


'#takes care of admin login'
@app.route('/admin', methods = ['GET', 'POST'])
def adm():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == 'bill' and password == '123':
            return render_template("adminTrue.html", user = username)

    return render_template("adminLogin.html")

'#takes care of app find names by gender without login'
@app.route('/')
@app.route('/send', methods =['GET', 'POST'])
def send():

    if request.method == 'POST':
        myname = request.form['name']
        gender = utilities.gender.find_gender_with_api(myname)
        return render_template("gender.html", name = myname, gender = gender)

    return render_template("index.html")


if __name__ == "__main__":
    app.run()


