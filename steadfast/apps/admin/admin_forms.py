
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask.ext.wtf import Form
from wtforms import (TextField,
                     PasswordField,
                     SubmitField,
                     FileField,
                     HiddenField,
                     StringField,
                     TextAreaField)
from wtforms.widgets import TextArea
################################

### Local Imports ###

################################


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super().__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class UserForm(Form):
    username = TextField("username")
    password = PasswordField("password")


class JobDescription(Form):
    title = TextField("position title")
    body = CKTextAreaField()
