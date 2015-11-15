
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask import render_template, redirect, url_for, request
from flask.views import View, MethodView
from bson.objectid import ObjectId
################################

### Local Imports ###
from steadfast.apps.careers import careers
from steadfast import lm, mongo
################################


class Index(MethodView):
    def get(self):
        all_jobs = mongo.db.jobs.find()

        return render_template('/careers/index.html', all_jobs=all_jobs)

    def post(self):
        searched_job = request.form.get("search")
        return redirect(url_for("careers.Search", searched_job=searched_job))


class Job(View):
    def dispatch_request(self, job_id):
        job = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})
        return render_template('/careers/job.html', job=job)


class Search(MethodView):
    def get(self, searched_job):
        jobs = mongo.db.jobs.find({"title":
                                  {"$regex": searched_job,
                                   "$options": "i"}})
        return render_template('/careers/search.html', jobs=jobs)

    def post(self, searched_job):
        searched_job = request.form.get("search")
        return redirect(url_for("careers.Search", searched_job=searched_job))

careers.add_url_rule('/',
                     view_func=Index.as_view('Index'),
                     methods=['GET', 'POST'])
careers.add_url_rule('/job/<job_id>',
                     view_func=Job.as_view('Job'),
                     methods=['GET'])
careers.add_url_rule('/search/<searched_job>',
                     view_func=Search.as_view('Search'),
                     methods=['GET', 'POST'])



