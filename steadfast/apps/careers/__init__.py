
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask import Blueprint
################################

### Local Imports ###

################################


careers = Blueprint('careers', __name__)
from .views import *

