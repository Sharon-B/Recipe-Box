from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
                     TextAreaField, SubmitField)
from wtforms.validators import InputRequired, Length, Email


# Create RegisterForm class which inherits from FLaskForm
class RegisterForm(FlaskForm):
    username = StringField(
        'username', validators=[InputRequired()],
        render_kw={"placeholder": "Username"})
    password = PasswordField(
        'password', validators=[InputRequired(), Length(min=6, max=16)],
        render_kw={"placeholder": "Password"})
    email = StringField(
        'email', validators=[InputRequired(),
                             Email()],
        render_kw={"placeholder": "Email"})
