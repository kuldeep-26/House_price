from flask import Flask,render_template,url_for,request

import joblib
model = joblib.load('./models/randomforest_model.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route("/prediction", methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        # Input values
        area = int(request.form['area'])

        bedroom = int(request.form['bedroom'])

        bathroom = int(request.form['bathroom'])

        guestroom = int(request.form['guestroom'])

        story = int(request.form['story'])

        basement = int(request.form['basement'])

        furnishing = request.form['furnishing']
        furnished = 0
        Semi_furnished = 0
        if furnishing == 'Furnished':
            furnished = 1
        elif furnishing == 'Semi Furnished':
            Semi_furnished = 1

        ac = int(request.form['ac'])

        parking = int(request.form['parking'])

        main_road = int(request.form['main_road'])


        unseen_data = [area,bedroom,bathroom,guestroom,story,basement,furnished,Semi_furnished,ac,parking,main_road]

        prediction = model.predict([unseen_data])[0]
        prediction = round(prediction,2)
            
        return render_template('output.html', prediction=prediction,
                               area = area,
                               bedroom = bedroom,
                               bathroom = bathroom,
                               guestroom = 'Yes' if guestroom == 1 else 'No',
                               story = story,
                               basement = 'Yes' if basement == 1 else 'No',
                               furnishing = furnishing,
                               ac = 'Yes' if ac == 1 else 'No',
                               parking = parking,
                               main_road = 'Yes' if main_road == 1 else 'No'
                               )  # Pass the prediction to the template

if __name__ == "__main__":
    app.run(debug=True)