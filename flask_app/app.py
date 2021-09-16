from flask import Flask, render_template, request
import joblib
app = Flask(__name__)
model = joblib.load('diabetic_79.pkl')
@app.route('/')
def hellow():
    return render_template('form.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/contacts')
def contacts():
    return 'welcome to contacts'

@app.route('/submit', methods = ["POST"])
def form_page():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    # print(fname, sname, phone, email)
    result = model.predict([[preg, plas, pres, skin, test,mass,pedi,age]])
    # print(result)

    if result[0]==1:
        out = 'person is diabetic'
    else:
        out = 'person is not diabetic'
    return render_template('data_sent.html', data = f'{out}')
if __name__ == '__main__':
    app.run(debug=True)
