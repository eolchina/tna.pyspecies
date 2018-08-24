from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class TaxonForm(Form):
    name = StringField('Name', validators=[Required()])
    submit = SubmitField('Submit')

# class TaxonForm(Form):
#     name = StringField('Name', validators=[Required()])
#     submit = SubmitField('Submit')

class DisForm(Form):
    distribution = StringField('Distribution', validators=[Required()])
    submit = SubmitField('Submit')


class IucnForm(Form):
    category = StringField('IUCN Category:', validators=[Required()])
    submit = SubmitField('Submit')
