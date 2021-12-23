from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, \
    BooleanField, SelectField, IntegerField, SelectMultipleField, PasswordField, \
    DateTimeField
from flask_ckeditor import CKEditorField
# from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, ValidationError

from .models import Product, MyEnum

def check_digits(form, string):
    if not string.data.isdigit():
        raise ValidationError('Поле повинно містити тільки цифри')

class FormProductCreate(FlaskForm):

    codeOfProduct = StringField(
            'Code Of product',
            validators=[DataRequired(message="Поле не можу бути пустим!"),
                        check_digits],
            render_kw={'size':31}
        )
    name = StringField(
            'Name',
            validators=[DataRequired(message="Поле не можу бути пустим!")],
            render_kw={'size':31}
        )
    typeOfProduct = SelectField(
        'Type Of product',
        choices=[('materials', 'materials'), ('products', 'products'),
                 ('ware', 'ware'), ('industrial', 'industrial'),
                 ('electronics', 'electronics')]
    )
    is_product =  BooleanField(
            'Is product'
        )
    count = StringField(
            'Count',
            validators=[DataRequired(message="Поле не можу бути пустим!"),
                        check_digits],
            render_kw={'size':31}
        )
    price = StringField(
        'Price',
        validators=[DataRequired(message="Поле не можу бути пустим!"),
                    check_digits],
        render_kw={'size': 31}
    )
    description = TextAreaField(
            'Descryption',
            validators=[
                DataRequired(),
                Length(min=3, max=80, message="Field must be between 3 and 150 characters long!")
            ],
            render_kw={'cols':35, 'rows': 5}
        )

    submit = SubmitField('Створити')


class FormProductUpdate(FlaskForm):

    codeOfProduct = StringField(
            'Code Of product',
            validators=[DataRequired(message="Поле не можу бути пустим!"),
                        check_digits],
            render_kw={'size':31}
        )
    name = StringField(
            'Name',
            validators=[DataRequired(message="Поле не можу бути пустим!")],
            render_kw={'size':31}
        )
    typeOfProduct = SelectField(
        'Type Of product',
        choices=[('materials', 'materials'), ('products', 'products'),
                 ('ware', 'ware'), ('industrial', 'industrial'),
                 ('electronics', 'electronics')]
    )
    is_product =  BooleanField(
            'Is product'
        )
    count = StringField(
            'Count',
            validators=[DataRequired(message="Поле не можу бути пустим!"),
                        check_digits],
            render_kw={'size':31}
        )
    price = StringField(
        'Price',
        validators=[DataRequired(message="Поле не можу бути пустим!"),
                    check_digits],
        render_kw={'size': 31}
    )
    description = TextAreaField(
            'Descryption',
            validators=[
                DataRequired(),
                Length(min=3, max=80, message="Field must be between 3 and 150 characters long!")
            ],
            render_kw={'cols':35, 'rows': 5}
        )

    submit = SubmitField('Оновити')