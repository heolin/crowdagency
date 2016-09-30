# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heolin123$crowdhub',
        'USER': 'heolin123',
        'PASSWORD': 'Password321',
        'HOST': 'heolin123.mysql.pythonanywhere-services.com',
    }
}


# Setup mongo connection
#MONGO_DATABASE_NAME = 'crowdhub_data'
#from mongoengine import connect
#DEFAULT_CONNECTION_NAME = connect(MONGO_DATABASE_NAME)

