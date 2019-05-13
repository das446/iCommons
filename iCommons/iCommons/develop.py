from .settings import *

DEBUG = False

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

STATIC_ROOT = (
   '/var/webapps/static/'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/webapps/db/db.sqlite3',
    }
}
DATABASE_NAME = '/var/webapps/db/db.sqlite3'
ALLOWED_HOSTS = ['rack113.cs.drexel.edu', '129.25.13.213']

#ihelp_email = "ihelp@drexel.edu"

IHELP_EMAIL = "ihelptesting@gmail.com"

URL = "http://rack113.cs.drexel.edu"