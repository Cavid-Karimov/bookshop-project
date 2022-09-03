from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,EmailField,PasswordField
from wtforms.validators import DataRequired, Length


class RegistrForm(FlaskForm):
    currency = StringField(label="First name:", validators=[DataRequired(), Length(min=3, max=60)],render_kw={"placeholder": "Your first name"})
    first_name = StringField(label="First name:", validators=[DataRequired(), Length(min=3, max=60)],render_kw={"placeholder": "Your first name"})
    last_name = StringField(label="Last name:", validators=[DataRequired(), Length(min=3, max=60)],render_kw={"placeholder": "Your last name"})
    phone_number = StringField(label="Email", validators=[DataRequired(), Length(min=10, max=60)],render_kw={"placeholder": "Your Email"})
    code = StringField(label="Kod", validators=[DataRequired(), Length(min=8, max=60)],render_kw={"placeholder": "Your password"})
    kampus = StringField(label="Filial", validators=[DataRequired(), Length(min=8, max=60)],render_kw={"placeholder": "Your password"})
