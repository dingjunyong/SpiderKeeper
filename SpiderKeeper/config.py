# Statement for enabling the development environment
import os

DEBUG = True

# Define the application directory


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath('.'), 'SpiderKeeper.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@192.168.1.252:3306/scrapy'
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# log
LOG_LEVEL = 'INFO'

# spider services
SERVER_TYPE = 'scrapyd'
SERVERS = ['http://192.168.1.250:6800']

# basic auth
NO_AUTH = True
BASIC_AUTH_USERNAME = 'admin'
BASIC_AUTH_PASSWORD = 'admin'
BASIC_AUTH_FORCE = True
