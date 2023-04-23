from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,SelectField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterUser(FlaskForm):
    name = StringField("UserName",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    gender = SelectField(u'Gender', choices=["Male","Female"])
    submit = SubmitField("Sign Me Up")

class LoginUser(FlaskForm):
    email = StringField("Email",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Log In")

class Comment_wtf(FlaskForm):
    comment = CKEditorField('Add Comment Here :')
    submit = SubmitField('Submit Comment')