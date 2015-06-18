#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'David Moser'
SITENAME = u'No Antidote for Anhedonia'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Static paths will be copied without parsing
STATIC_PATHS = ['images', 'pages', 'extra/CNAME']

# Shift the installed location of a file
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

# Sole author
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('the Working Computer', 'http://theworkingcomputer.com'),
         ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Themes and plugins
THEME = "pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'darkly'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['share_post',
           'pelican-bootstrapify',
           'pelican_comment_system',
           'neighbors',]

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Contact
EMAIL_ADDR = 'david at theworkingcomputer dot com'
