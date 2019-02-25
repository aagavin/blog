#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#   - pip install -r requirements.txt
# script:
#   - pelican content/
AUTHOR = 'aaron'
SITENAME = 'aBlog'
SITEURL = ''
STATIC_PATHS = ['__images', 'pdfs', 'favicon.png', 'favicon.ico']

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Feedburner', 'http://feeds.feedburner.com/aagavin/blog'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme settings
# https://github.com/nasskach/pelican-blueidea/
THEME = 'theme/pelican-blueidea'
DISPLAY_SEARCH_FORM = True
DISPLAY_CATEGORIES_ON_SUBMENU = True