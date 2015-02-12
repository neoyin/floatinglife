#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Neo'
SITENAME = u'\u6d6e\u751f\u82e5\u68a6'
SITEURL = 'http://www.floatinglife.cn'
THEME = 'theme/tuxlite_zf'
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'
LOCALE = ("zh_CN")

DISPLAY_PAGES_ON_MENU = True
SUMMARY_MAX_LENGTH = 50

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

#plugins
PLUGIN_PATHS = ['plugins']

PLUGINS = ['related_posts']
RELATED_POSTS_MAX = 6


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('枫桥夜泊', 'http://fancy.floatinglife.cn'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
