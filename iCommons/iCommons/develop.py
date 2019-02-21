from .settings import *

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/webapps/db/db.sqlite3',
    }
}
DATABASE_NAME = '/var/webapps/db/db.sqlite3'
ALLOWED_HOSTS = ['rack113.cs.drexel.edu', '129.25.13.213']

EMAIL_BACKEND = "sgbackend.SendGridBackend"

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'das446drexel'
EMAIL_HOST_PASSWORD = '##sk34syyz'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SENDGRID_API_KEY = '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'