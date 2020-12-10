from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange, Optional
from benefactors.models import User, genderEnum, statusEnum, categoryEnum
from benefactors.helper.postalCodeManager import postalCodeManager


# -------------------------------------------------Login/Logout---------------------------------------------------------

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    Description = TextAreaField('Description', validators= [DataRequired()])
    submit = SubmitField('Submit')

class DeliveryRequestForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    tracking_number = StringField('Tracking Number', validators=[DataRequired(), Length(max=40)])
    submit = SubmitField('Post')


# ----------------------------------------------------SignUp------------------------------------------------------------

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    phone_number = StringField('Phone ', validators=[DataRequired(), Length(min=10, max=16)])
    postal_code = StringField('Postal Code ', validators=[DataRequired(), Length(max=10)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=60)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('There is an existing account associated with this email.')

    def validate_postal_code(self, postal_code):
        pcm = postalCodeManager()
        pc = postal_code.data.replace(" ", "").upper()
        if not pcm.verifyPostalCode(pc):
            raise ValidationError('That is not a valid Postal Code.')

    def validate_phone_number(self, phone_number):
        if not phone_number.data.isnumeric():
            raise ValidationError('phone number must consist of only integers')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken.')
            return
        allowed_symbols = ['_', '.']
        for c in username.data:
            if ( not c.isalpha() ) and ( not c.isnumeric() ) and ( c not in allowed_symbols ):
                raise ValidationError("username must only be made out of numbers and characters - only symbols allowed are '_ .' ")

# ---------------------------------------------------Forgot Pass--------------------------------------------------------

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account associated with the email.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=60)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')


# ----------------------------------------------------Posts-------------------------------------------------------------

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    category = SelectField('Category')
    submit = SubmitField('Post')


# -----------------------------------------------------Account----------------------------------------------------------

class AccountUpdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    phone_number = StringField('Phone ', validators=[DataRequired(), Length(min=10,max=16)])
    postal_code = StringField('Postal Code ', validators=[DataRequired(), Length(max=6)])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is taken.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('There is an existing account associated with this email.')

    def validate_postal_code(self, postal_code):
        pcm = postalCodeManager()
        if not pcm.verifyPostalCode(postal_code.data):
            raise ValidationError('That is not a valid Postal Code.')

    def validate_phone_number(self, phone_number):
        if not phone_number.data.isnumeric():
            raise ValidationError('phone number must consist of only integers')
# ----------------------------------------------------Comments----------------------------------------------------------

class PostCommentForm(FlaskForm):
    comment_desc = TextAreaField('Comment', validators=[DataRequired()])
    submit_comment = SubmitField('Submit Comment')

    def validate_commentdesc(self, comment_desc):
        if comment_desc.data.strip() == "":
            raise ValidationError('Comment cannot be empty')


# ------------------------------------------------------Messages--------------------------------------------------------

class SendMessageForm(FlaskForm):
    chat_message_desc = TextAreaField('', validators=[DataRequired(), Length(min=1, max=1024)])
    submit_chatmsg = SubmitField('Send Message')

    def validate_chat_message_desc(self, chat_message_desc):
        if chat_message_desc.data.strip() == "":
            raise ValidationError('Message cannot be empty')


# ----------------------------------------------------Reviews-----------------------------------------------------------

class ReviewForm(FlaskForm):
    description = TextAreaField('Review')
    score = DecimalField('Rate - (1 to 10) ', validators=[DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField('Submit')


# ----------------------------------------------------Search------------------------------------------------------------

class SearchForm(FlaskForm):
    searchString = StringField('Search Title', validators=[Length(max=100)])
    postalCode = StringField('Postal Code', validators=[Optional()])
    gSuggest = BooleanField('gSuggest', default=False)
    radius = IntegerField('Radius(Km)', validators=[Optional(), NumberRange(min=1, max=100)])
    status = SelectField('Status',
                         choices=[('all', 'All'), (statusEnum.OPEN.name, 'Open'), (statusEnum.TAKEN.name, 'Taken'),
                                  (statusEnum.CLOSED.name, 'Closed')])
    category = SelectField('Category')
    updateSearch = SubmitField('Apply Filters')

    def validate_postal_code(self, postal_code):
        pcm = postalCodeManager()
        if not pcm.verifyPostalCode(postal_code.data):
            raise ValidationError('That is not a valid Postal Code.')


# ----------------------------------------------------Payments----------------------------------------------------------

class DonationForm(FlaskForm):
    amount = IntegerField('Amount', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Pay with Card')
