#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jeferson Daniel'
SITENAME = u'Jeferson Daniel'
SITESUBTITLE = u'Desenvolvedor Web'
SITEURL = 'https://jefersondaniel.com'
DISQUS_SITENAME = "jefersondaniel"
DESCRIPTION = 'Um blog sobre desenvolvimento web, programação e tudo mais'
KEYWORDS = 'python, django, flask, javascript, php, laravel, mobile, android, framework, agile, programação'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_RSS = 'feed.xml'
DEFAULT_PAGINATION = 10
RELATIVE_URLS = True

THEME = "themes/Just-Read"

ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TEMPLATE_PAGES = {'blog.html': 'blog/index.html'}

SOCIAL = (
    ('GitHub',  'http://github.com/jefersondaniel'),
    ('Linkedin',  'http://br.linkedin.com/pub/jeferson-daniel/53/66a/46a'),
)

STATIC_PATHS = ['extra/CNAME', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

PLUGINS = [
    'minification'
]
