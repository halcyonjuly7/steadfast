

from flask_admin.contrib.pymongo import ModelView
from flask.ext.login import UserMixin



from .admin_forms import UserForm, JobDescription


class UserModel(ModelView):
    column_list = ("username", "password")
    form = UserForm


class JobModel(ModelView):
    column_list = ("title", "body")
    form = JobDescription

    create_template = "admin_templates/misc_admin_templates/admin_careers_create_template.html"
    edit_template = "admin_templates/misc_admin_templates/admin_careers_edit_template.html"



class User(UserMixin):
    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username
