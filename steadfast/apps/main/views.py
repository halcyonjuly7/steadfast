
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask import render_template, redirect, url_for, request
from flask_mail import Message
from flask.views import View, MethodView
################################

### Local Imports ###
from steadfast.apps.main import main
from steadfast import mail, mongo
################################


class Index(View):
    def dispatch_request(self):
        return render_template('/main/index.html')


class About(View):
    def dispatch_request(self):
        return render_template('/main/about.html')


class Contact(MethodView):
    def get(self):
        return render_template('/main/contact.html')

    def post(self):
        name = request.form.get("full_name")
        email = request.form.get("email")
        message = request.form.get("message")
        msg = Message(message,
                      sender=email,
                      recipients=["halcyonjuly7@gmail.com"])
        msg.body = """
        from {email}
        {message}
        - {name}
        """.format(email=email,
                   message=message,
                   name=name)
        mail.send(msg)
        return self.get()


class Gallery(View):
    def dispatch_request(self):
        return render_template('/main/gallery.html')


class Area(View):
    def dispatch_request(self):
        return render_template('/main/area.html')
        mongo.db.jobs.find_one({"title": job_id})
        return render_template('/main/job.html')


main.add_url_rule('/',
                  view_func=Index.as_view('Index'),
                  methods=['GET', 'POST'])
main.add_url_rule('/about',
                  view_func=About.as_view('About'),
                  methods=['GET', 'POST'])
main.add_url_rule('/contact',
                  view_func=Contact.as_view('Contact'),
                  methods=['GET', 'POST'])
main.add_url_rule('/gallery',
                  view_func=Gallery.as_view('Gallery'),
                  methods=['GET', 'POST'])
main.add_url_rule('/area',
                  view_func=Area.as_view('Area'),
                  methods=['GET', 'POST'])

