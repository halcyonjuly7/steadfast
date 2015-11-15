
from flask import render_template, redirect, url_for, request
from flask.ext.admin import AdminIndexView, expose
from flask.ext.login import (current_user,
                             login_required,
                             login_user,
                             logout_user)

from steadfast import lm, mongo
from .admin_models import User

@lm.user_loader
def load_user(username):
    return User(username)



class IndexView(AdminIndexView):##A

    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for("admin.login"))
        else:
            return self.render("admin_templates/admin_base.html")

    @expose("/login", methods=["GET", "POST"])
    def login(self):
        if request.method == "GET":
            return self.render("admin_templates/admin_login.html")
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            if mongo.db.users.find_one({"username": username,
                                        "password": password}) is not None:
                login_user(User(username))
                return redirect(url_for("admin.index"))
            return redirect(url_for("admin.login"))

    @expose("/logout", methods=["GET"])
    def logout(self):
        logout_user()
        return redirect(url_for("admin.login"))


