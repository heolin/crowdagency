from crowdhub.settings.base import *
from crowdhub.settings.auth import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heolin123$crowdhub',
        'USER': 'heolin123',
        'PASSWORD': 'Password321',
        'HOST': '127.0.0.1',
        'PORT': '3333',
    }
}


# Setup mongo connection
MONGO_DATABASE_NAME = 'crowdhub_data'
from mongoengine import connect
DEFAULT_CONNECTION_NAME = connect(MONGO_DATABASE_NAME,
                                  host="mongodb://heolin123:Password321@ds033337.mongolab.com:33337/crowdhub")

