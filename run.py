
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask.ext.admin import Admin
#################################

### Local Imports ###
from steadfast import create_app, mongo
from steadfast.apps.admin.admin_views import IndexView
from steadfast.apps.admin.admin_models import UserModel, JobModel

#################################

if __name__ == "__main__":
    app = create_app("config")
    with app.app_context():
        admin = Admin(app,
                      index_view=IndexView())
        admin.add_view(UserModel(mongo.db.users, endpoint="users"))
        admin.add_view(JobModel(mongo.db.jobs, endpoint="job_openings"))
    app.run()


  