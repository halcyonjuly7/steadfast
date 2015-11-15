### Standard Library Imports ###
import os
################################

### 3rd Party Imports ###

################################

### Local Imports ###

################################

DEBUG = True
SQALCHEMY_DATABASE_URI = "sqlite:/// + os.path.join(os.path.dirname(__file__), ../data-dev.sqlite3 "
SECRET_KEY = "secret123456"
###FLASK-MAIL###
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'halcyonjuly7@gmail.com'
MAIL_PASSWORD = 'Jiujitsu' 
MONGO_DBNAME ="Steadfast"
