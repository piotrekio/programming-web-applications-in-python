import flask_wtf
from wtforms import StringField
from wtforms import widgets
from wtforms import validators


class CreateForm(flask_wtf.Form):
    title = StringField(
        validators=[validators.input_required()])
    content = StringField(
        validators=[validators.input_required()],
        widget=widgets.TextArea())
