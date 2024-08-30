from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, DataRequired, Length, Email
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
bootstrap = Bootstrap5(app)

class LoginForm(FlaskForm):
    email = EmailField('email', validators=[InputRequired(), 
                                             Length(min=6, message='Too short. You sure this is an actual email address?'),
                                             Email(message="That's not a valid email address")])
    password = PasswordField('password', validators=[InputRequired(), 
                                                     Length(min=8, message="Password must be at least 8 characters longn")])
    submit = SubmitField('submit')

def check_credentials(user_email: str, user_password: str) -> bool:
    return user_email == "admin@email.com" and user_password == "12345678"



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data
        if check_credentials(user_email=user_email, user_password=user_password):
            return render_template("success.html")
        else: 
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
