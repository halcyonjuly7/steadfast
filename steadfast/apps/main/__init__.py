
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask import Blueprint
################################

### Local Imports ###

################################


main = Blueprint('main', __name__)
from .views import *

