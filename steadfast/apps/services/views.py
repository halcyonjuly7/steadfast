
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask import render_template, redirect, url_for
from flask.views import View
################################

### Local Imports ###
from steadfast.apps.services import services
################################


class Index(View):
    def dispatch_request(self):
        return render_template('/services/index.html')


class Nursing(View):
    def dispatch_request(self):
        return render_template('/services/nursing.html')


class Pt(View):
    def dispatch_request(self):
        return render_template('/services/physical_therapy.html')


class Ot(View):
    def dispatch_request(self):
        return render_template('/services/occupational_therapy.html')


class Speech(View):
    def dispatch_request(self):
        return render_template('/services/speech_therapy.html')


class Social(View):
    def dispatch_request(self):
        return render_template('/services/social.html')


class Aide(View):
    def dispatch_request(self):
        return render_template('/services/aide.html')


services.add_url_rule('/nursing',
                      view_func=Nursing.as_view('Nursing'),
                      methods=['GET', 'POST'])
services.add_url_rule('/physical therapy',
                      view_func=Pt.as_view('Pt'),
                      methods=['GET', 'POST'])
services.add_url_rule('/occupational therapy',
                      view_func=Ot.as_view('Ot'),
                      methods=['GET', 'POST'])
services.add_url_rule('/speech therapy',
                      view_func=Speech.as_view('Speech'),
                      methods=['GET', 'POST'])
services.add_url_rule('/social work',
                      view_func=Social.as_view('Social'),
                      methods=['GET', 'POST'])
services.add_url_rule('/home health aide',
                      view_func=Aide.as_view('Aide'),
                      methods=['GET', 'POST'])
services.add_url_rule('/',
                      view_func=Index.as_view('Index'),
                      methods=['GET', 'POST'])
