from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from settings import MAX_URL_LENGTH, MAX_SHORT_URL_LENGTH, VALID_SYMBOLS


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(max=MAX_URL_LENGTH),
            URL(message='Введите корректный URL адрес')
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(max=MAX_SHORT_URL_LENGTH),
            Regexp(
                VALID_SYMBOLS,
                message="Допустимы только цифры и латинские буквы"
            )
        ]
    )
    submit = SubmitField('Добавить')
