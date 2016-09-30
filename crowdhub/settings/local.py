from crowdhub.settings.base import *
from crowdhub.settings.auth import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crowdhub',
        'USER': 'root',
        'PASSWORD': 'password',
       'HOST': 'localhost',
    }

}


# Setup mongo connection
MONGO_DATABASE_NAME = 'crowdhub_data'
from mongoengine import connect
DEFAULT_CONNECTION_NAME = connect(MONGO_DATABASE_NAME)

