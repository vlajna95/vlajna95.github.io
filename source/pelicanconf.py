#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from datetime import datetime

def years():
	start_year = 2020
	year = datetime.now().year
	if start_year == year:
		return "{}".format(year)
	else:
		return (start_year, year, "{}-{}".format(start_year, year))

the_years = years()

LANGUAGES_LOOKUP = {
	"en": "English",
	"es": "Español",
	"sr": "Srpski",
}

def lookup_lang_name(lang_code):
	return LANGUAGES_LOOKUP[lang_code]


AUTHOR = "Danijela Popović"
SITENAME = "DP Tech"
SITESUBTITLE = "Tvoj omiljeni blog"
SITEURL = "http://vlajna95.github.io"

THEME = "themes/brownstone"
LOGO = "logo_transparent.png"
COPYRIGHT = "Copyright © " + the_years[2] + " " + SITENAME + ". Sva prava zadržana."
DISPLAY_BREADCRUMBS = True

PATH = "content"
PATH_METADATA = "(?P<category>.*)/.*"
STATIC_PATHS = ["audio", "images"]

ARTICLE_URL = "articles/{slug}"
ARTICLE_SAVE_AS = "articles/{slug}/index.html"
PAGE_URL = "pages/{slug}"
PAGE_SAVE_AS = "pages/{slug}/index.html"
CATEGORY_URL = "categories/{slug}"
CATEGORY_SAVE_AS = "categories/{slug}/index.html"

FEED_ALL_ATOM = "feeds/atom/all.xml"
CATEGORY_FEED_ATOM = "feeds/atom/{slug}.xml"
TAG_FEED_ATOM = "feeds/atom/tag-{slug}.xml"
TRANSLATION_FEED_ATOM = "feeds/atom/{lang}-all.xml"
FEED_ALL_RSS = "feeds/rss/all.xml"
CATEGORY_FEED_RSS = "feeds/rss/{slug}.xml"
TAG_FEED_RSS = "feeds/rss/tag-{slug}.xml"
TRANSLATION_FEED_ATOM = "feeds/rss/{lang}-all.xml"
RSS_FEED_SUMMARY_ONLY = True

# Blogroll
LINKS = (("DaniMundo", "http://danimundo.com"), ("Pelican", "https://getpelican.com/"))

# Social widget
SOCIAL = (
	("Facebook", "https://fb.me/dani.vlajna"),
	("Twitter", "https://twitter.com/DJ_Dani_Serbia"),
	("YouTube", "https://www.youtube.com/DanijelaPopovic"),
	("Github", "https://github.com/vlajna95"),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SEO_REPORT = True
SEO_ENHANCER = True
SEO_ENHANCER_OPEN_GRAPH = True

SITEMAP = {
	"format": "xml",
	"priorities": {
		"articles": 0.8,
		"indexes": 0.6,
		"pages": 0.8
	},
	"changefreqs": {
		"articles": "hourly",
		"indexes": "hourly",
		"pages": "daily"
	}
}

MARKDOWN = {
	"extension_configs": {
		"markdown.extensions.codehilite": {"css_class": "highlight"},
		"markdown.extensions.extra": {},
		"markdown.extensions.meta": {},
		"markdown.extensions.nl2br": {},
		"markdown.extensions.tables": {},
		"markdown.extensions.toc": {"title": ""},
		"cell_row_span": {},
		"pymdownx.emoji": {"title": "long"},
		"pymdownx.tasklist": {},
	},
	"output_format": "html5",
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["more_categories", "neighbors", "seo", "sitemap", "i18n_subsites", "readtime"]

JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.do", "jinja2.ext.i18n"]}
JINJA_FILTERS = {
	"lookup_lang_name": lookup_lang_name,
}

DEFAULT_LANG = "sr"
LOCALE = DEFAULT_LANG
TIMEZONE = "Europe/Belgrade"
DEFAULT_DATE_FORMAT = "%A, %-d. %B %Y. u %H:%M"

# I18N_GETTEXT_LOCALEDIR = "translations"
I18N_GETTEXT_DOMAIN = "dp_tech"
I18N_SUBSITES = {
	"en": {
		"SITESUBTITLE": "Your favorite tech blog :smile:",
		"COPYRIGHT": "Copyright © " + the_years[2] + " " + SITENAME + ". All rights reserved.",
		"LOCALE": "en",
		"DEFAULT_DATE_FORMAT": "%A, %B %-d, %Y at %H:%M",
	},
	"es": {
		"SITESUBTITLE": "Tu blog preferido",
		"COPYRIGHT": "Copyright © " + the_years[2] + " " + SITENAME + ". Todos los derechos reservados.",
		"LOCALE": "es",
		"TIMEZONE": "Europe/Madrid",
		"DEFAULT_DATE_FORMAT": "%A, %-d de %B de %Y a las %H:%M",
	},
}
"""
	"sr": {
		"SITESUBTITLE": "Tvoj omiljeni blog",
		"COPYRIGHT": "Copyright © " + the_years[2] + " " + SITENAME + ". All rights reserved.",
		"LOCALE": "sr_RS.utf8@latin",
		"TIMEZONE": "Europe/Belgrade",
		"DEFAULT_DATE_FORMAT": "%A, %-d. %B %Y. u %H:%M",
	}
"""