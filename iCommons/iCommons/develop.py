from .settings import *

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

DATABASE_NAME = '/var/webapps/db/db.sqlite3'
ALLOWED_HOSTS = ['rack113.cs.drexel.edu', '129.25.13.213']