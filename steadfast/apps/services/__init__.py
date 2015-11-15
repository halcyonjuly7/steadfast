
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask import Blueprint
################################

### Local Imports ###

################################


services = Blueprint('services', __name__)
from .views import *

