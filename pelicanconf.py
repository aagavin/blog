#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aaron'
SITENAME = 'aBlog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['__images', 'pdfs']

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Theme settings
# THEME = './pelican-themes/attila'
# THEME = './pelican-themes/clean-blog'
# THEME = './pelican-themes/genus'
# THEME = './pelican-themes/html5-dopetrope'
THEME = './theme/octopress'
# THEME = './pelican-themes/pelican-cait'
# THEME = './pelican-themes/semantic-ui'

# THEME = './pelican-themes/tuxlite_zf'???
# THEME = './pelican-themes/zurb-F5-basic'


### THEME CONFIG
GITHUB_USER = 'aagavin'
GITHUB_REPO_COUNT = 5
GITHUB_SHOW_USER_LINK = True

DISPLAY_PAGES_ON_MENU = True


SIDEBAR_IMAGE = '__images/profile.png'
# SEARCH_BOX = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
