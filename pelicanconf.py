#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'David Moser'
SITENAME = u'No Antidote for Anhedonia'
SITEURL = 'http://twc-blog.theworkingcomputer.com'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Static paths will be copied without parsing
STATIC_PATHS = ['images', 'pages', 'extra/CNAME']

# Shift the installed location of a file
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

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
           'pelican_comment_system',
           'neighbors',]
TYPOGRIFY = True

# uncomment below to enable pelican_comment_system
#PELICAN_COMMENT_SYSTEM = True

# enable disqus comments on site
DISQUS_SITENAME = "twc-blog.disqus.com"

# Social widget
#SOCIAL = (('Facebook', 'facebook.com'),
#         ('Reddit', 'reddit.com'),
#         ('Hacker News', 'news.ycombinator.com'))


DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Contact
EMAIL_ADDR = 'david at theworkingcomputer dot com'
