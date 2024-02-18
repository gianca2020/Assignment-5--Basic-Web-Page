from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
#import os

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'giancarloforero@gmail.com'
app.config['MAIL_PASSWORD'] = '**********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('page.html')


@app.route('/submit-form', methods=['POST'])
def submit_form():
    print("Submitted")
    try:
        name = request.form['name']
        email = request.form['email']
        body = request.form['body']

        msg = Message("Here is this email " + name,
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[email])
        msg.body = body
        mail.send(msg)
    except Exception as e:
        print(e)

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
