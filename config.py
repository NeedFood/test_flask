#!/usr/bin/env python


import os


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/<username>'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com/<username>'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com/<username>'}
]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


# mail server settings
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = True
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('cnstding@gmail.com')
MAIL_PASSWORD = os.environ.get('pxdyp19941123')



# administrator list
ADMINS = ['cnstding@gmail.com']


#pagination
POST_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'search.db')

MAX_SEARCH_RESULTS = 50

LANGUAGES = {
    'en': 'English',
    'zh': 'Chinese'
}
