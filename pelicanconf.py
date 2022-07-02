#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
from datetime import datetime
from jinja2 import Environment, ChoiceLoader, FileSystemLoader
from markdown import Markdown


MARKDOWN = {
	"extension_configs": {
		"markdown.extensions.attr_list": {},
		"markdown.extensions.def_list": {},
		"markdown.extensions.footnotes": {},
		"markdown.extensions.md_in_html": {},
		"markdown.extensions.meta": {},
		"markdown.extensions.nl2br": {},
		"markdown.extensions.tables": {},
		"markdown.extensions.toc": {"title": "", "toc_depth": "2-6"},
		"pymdownx.emoji": {"title": "long"},
		"pymdownx.caret": {},
		"pymdownx.tilde": {},
		"pymdownx.mark": {},
		"pymdownx.tasklist": {},
		"pymdownx.details": {},
		"pymdownx.superfences": {"preserve_tabs": True},
		"pymdownx.highlight": {"css_class": "highlight", "use_pygments": True, "noclasses": True, "pygments_style": "Dani_dark"},
		# "markdown.extensions.iconfonts": {"prefix_base_pairs": {"fa-": "fas"}},
		"customblocks": {"generators": {"question": "customblocks.custom_generators:question"}}, # {"generators": {"youtube": {}, "linkcard": {}}},
		"tablespan": {},
		"mdx_include_lines": {"base_path": "content/code", "encoding": "utf-8", "line_nums": False},
		"markdown_include.include": {"encoding": "utf-8"},
		# "tweetable": {"networks": ("twitter", "facebook"), "snippet": """<div class="tweetable" role="blockquote">
		# <p>{quote}</p>
		# <p class="tweetable-buttons">{buttons}</p>
		# </div>""", "snippet_twitter": """<a class="tweetable-button" title="Tweet" href="https://twitter.com/intent/tweet?text={quote}&url={urlq}&hashtags={hashtags}" target="_blank">{icon_twitter}</a>""", "snippet_facebook": """<a class="tweetable-button" title="Kopiraj tekst i klikni ovde da ga podeliš na Facebook." href="https://www.facebook.com/sharer/sharer.php?u={urlq}" target="_blank">{icon_facebook}</a>"""},
	},
	"output_format": "html5"
}
# "markdown.extensions.codehilite": {"use_pygments": True, "css_class": "highlight"}, "martor.extensions.emoji": {} # "cell_row_span": {}, "customblocks": {"generators": {"youtube_playlist": "md_cb:youtube_playlist"}, "config": {"youtube_inlineFluidStyle": True}}, "magic": {}, "tweetable": {"networks": ("twitter", "facebook")}, "markdown_del_ins": {}, "iconfonts": {"prefix_base_pairs": {"fa-": "fa", "glyph-": "glyphicon"}}}

md_extensions = [e for e in MARKDOWN["extension_configs"].keys()]
md = Markdown(extensions=md_extensions, extension_configs=MARKDOWN["extension_configs"], output_format="html5")

JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.do", "jinja2.ext.i18n"]}

def years():
	start_year = 2020
	year = datetime.now().year
	if start_year == year:
		return "{}".format(year)
	else:
		return (start_year, year, "{}-{}".format(start_year, year))

the_years = years()

LANGUAGES_LOOKUP = {
	"sr": "Srpski",
	"es": "Español",
	"ca": "Català",
	"en": "English",
}

def lookup_lang_name(lang_code):
	return LANGUAGES_LOOKUP[lang_code]

def category_details(cat_name):
	if not cat_name in CATEGORY_DETAILS.keys():
		return ""
	cat_details_obj = CATEGORY_DETAILS[cat_name]
	if cat_details_obj.long_description != "":
		env = Environment(loader=ChoiceLoader([FileSystemLoader(os.path.join("themes", "Elegant", "templates"))]), **JINJA_ENVIRONMENT)
		jinja_processed = env.from_string(cat_details_obj.long_description).render()
		return md.convert(jinja_processed)
	else:
		return cat_details_obj.short_description

JINJA_FILTERS = {
	"lookup_lang_name": lookup_lang_name,
	"cat_details": category_details,
}


AUTHOR = "Danijela Popović"
SITENAME = "DP Tech"
SITESUBTITLE = "Tvoj omiljeni blog"
# SITEURL = "http://tech.danimundo.com" # "http://vlajna95.github.io"
SITEURL = "http://localhost:8000"

THEME = "themes/Elegant"
LOGO = "logo_transparent.png"
COPYRIGHT = "Copyright © " + the_years[2] + " " + SITENAME + ". Sva prava zadržana."
DISPLAY_BREADCRUMBS = True

DELETE_OUTPUT_DIRECTORY = True
PATH = "content"
PATH_METADATA = "(?P<category>.*)/.*"
STATIC_PATHS = ["audio", "docs", "images"]

INDEX_SAVE_AS = "blog_index.html"
ARTICLE_URL = "articles/{slug}"
ARTICLE_SAVE_AS = "articles/{slug}/index.html"
PAGE_URL = "pages/{slug}"
PAGE_SAVE_AS = "pages/{slug}/index.html"
CATEGORY_URL = "categories/{slug}"
CATEGORY_SAVE_AS = "categories/{slug}/index.html"
TAG_URL = "tags/{slug}"
TAG_SAVE_AS = "tags/{slug}/index.html"
ARCHIVES_SAVE_AS = "archives/index.html"
YEAR_ARCHIVE_SAVE_AS = "archives/{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS = "archives/{date:%Y}/{date:%m}/index.html"
DAY_ARCHIVE_SAVE_AS = "archives/{date:%Y}/{date:%m}/{date:%d}/index.html"

AUTHOR_PAGE_PATH = "author_pages"
CATEGORY_PAGE_PATH = "category_pages"
TAG_PAGE_PATH = "tag_pages"

CATEGORY_DETAILS_PATH = "cat_details"

ARTICLE_EXCLUDES = [AUTHOR_PAGE_PATH, CATEGORY_PAGE_PATH, TAG_PAGE_PATH, CATEGORY_DETAILS_PATH, "code"]

DIRECT_TEMPLATES = ["index"] #, "category", "tag"]

SLUG_REGEX_SUBSTITUTIONS = [
	(r"[/]+", "_"),
	(r"[^\w\s-]", ""), # remove non-alphabetical/whitespace/'-' chars
	(r"(?u)\A\s*", ""), # strip leading whitespace
	(r"(?u)\s*\Z", ""), # strip trailing whitespace
	(r"[-\s]+", "-"), # reduce multiple whitespace or '-' to single '-'
]

FEED_ALL_ATOM = "feeds/atom/all.xml"
CATEGORY_FEED_ATOM = "feeds/atom/{slug}.xml"
TAG_FEED_ATOM = "feeds/atom/tag-{slug}.xml"
TRANSLATION_FEED_ATOM = "feeds/atom/{lang}-all.xml"
FEED_ALL_RSS = "feeds/rss/all.xml"
CATEGORY_FEED_RSS = "feeds/rss/{slug}.xml"
TAG_FEED_RSS = "feeds/rss/tag-{slug}.xml"
TRANSLATION_FEED_ATOM = "feeds/rss/{lang}-all.xml"
RSS_FEED_SUMMARY_ONLY = True

# Main menu
MENUITEMS = [
	("Katalonski - Català", "/categories/katalonski-catala")
]
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Blogroll
LINKS = [("DaniMundo", "http://danimundo.com"), ("Pelican", "https://getpelican.com/")]

# Social widget
SOCIAL = [
	("Facebook", "https://fb.me/dani.vlajna"),
	("Twitter", "https://twitter.com/DJ_Dani_Serbia"),
	("YouTube", "https://www.youtube.com/DanijelaPopovic"),
	("Github", "https://github.com/vlajna95"),
]

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

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["jinja2content", "neighbors", "seo", "sitemap", "i18n_subsites", "post_stats", "extract_toc", "series", "share_post", "readtime", "more_categories"] #, "autopages", "category_meta"]

WORDS_PER_MINUTE = 150
READING_TIME_LOWER_LIMIT = 1
SHARE_LINKS = [("facebook", "Facebook"), ("twitter", "Twitter"), ("WhatsApp", "whatsapp"), ("email", "Email"), ("linkedin", "LinkedIn"), ("reddit", "Reddit")]
TWITTER_USERNAME = "DJ_Dani_Serbia"
# FEATURED_IMAGE = "http://dp-tech.tk/images/logo_transparent.png"
LANDING_PAGE_TITLE = SITENAME + " — " + SITESUBTITLE + " ☺"
# FREELISTS_NAME = ""
# GITHUB_ACTIVITY_FEED = "https://github.com/vlajna95.atom"
# GITHUB_ACTIVITY_MAX_ENTRIES = 10
# PDF_STYLE = ["a4", "twelvepoint"]

# Theme labels
HOMEPAGE_TITLE = "Početna"
RELATED_POSTS_LABEL = "Povezani članci"
SOCIAL_PROFILE_LABEL = "Društvene mreže"
PROJECTS_TITLE = "Drugi projekti"
EMAIL_SUBSCRIPTION_LABEL = "Mejling lista za lakšu komunikaciju"
EMAIL_FIELD_PLACEHOLDER = "Unesi svoj email..."
SUBSCRIBE_BUTTON_TITLE = "Prijavi se"
SHARE_POST_INTRO = "Podeli:"
COMMENTS_INTRO = "Komentari"
SITE_LICENSE = ""
SITE_DESCRIPTION = "Tvoj omiljeni blog :)"
TOC_LABEL = "Sadržaj"
PREV_ARTICLE_LABEL = "Prethodno"
NEXT_ARTICLE_LABEL = "Sledeće"
ARTICLE_DATE_LABEL = "Objavljeno"
ARTICLE_LAST_UPDATED_LABEL = "Poslednja izmena"
ARTICLE_CATEGORY_LABEL = "Kategorija"
ARTICLE_TAGS_LABEL = "Oznake"
SEARCH_LABEL = "Pretraga"
SEARCH_DESCRIPTION = "Pretraga sajta"
READING_TIME_LABEL = "Vreme potrebno za čitanje"
TRANSLATIONS_INTRO = "Dostupni prevodi članka"
RECENT_ARTICLES_LABEL = "Najnoviji članci"

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
		"HOMEPAGE_TITLE": "Home",
		"RELATED_POSTS_LABEL": "Related articles",
		"SOCIAL_PROFILE_LABEL": "Social networks",
		"PROJECTS_TITLE": "Other projects",
		"EMAIL_SUBSCRIPTION_LABEL": "A mailing list for easier communication",
		"EMAIL_FIELD_PLACEHOLDER": "Type your email...",
		"SUBSCRIBE_BUTTON_TITLE": "Subscribe",
		"SHARE_POST_INTRO": "Share:",
		"COMMENTS_INTRO": "Comments",
		"SITE_LICENSE": "",
		"SITE_DESCRIPTION": "Your favorite blog :)",
		"TOC_LABEL": "Contents",
		"PREV_ARTICLE_LABEL": "Previous",
		"NEXT_ARTICLE_LABEL": "Next",
		"ARTICLE_DATE_LABEL": "Published",
		"ARTICLE_LAST_UPDATED_LABEL": "Last updated",
		"ARTICLE_CATEGORY_LABEL": "Category",
		"ARTICLE_TAGS_LABEL": "Tags",
		"SEARCH_LABEL": "Search",
		"SEARCH_DESCRIPTION": "Search of the website",
		"READING_TIME_LABEL": "Reading time estimation",
		"TRANSLATIONS_INTRO": "Available translations of the article",
		"RECENT_ARTICLES_LABEL": "Newest articles",
	},
	"es": {
		"SITESUBTITLE": "Tu blog preferido",
		"COPYRIGHT": "Copyright © " + the_years[2] + " " + SITENAME + ". Todos los derechos reservados.",
		"LOCALE": "es",
		"TIMEZONE": "Europe/Madrid",
		"DEFAULT_DATE_FORMAT": "%A, %-d de %B de %Y a las %H:%M",
		"HOMEPAGE_TITLE": "Inicio",
		"RELATED_POSTS_LABEL": "Artículos relacionados",
		"SOCIAL_PROFILE_LABEL": "Redes sociales",
		"PROJECTS_TITLE": "Otros proyectos",
		"EMAIL_SUBSCRIPTION_LABEL": "Lista de correo, para una comunicación más simple",
		"EMAIL_FIELD_PLACEHOLDER": "Tu dirección de correo...",
		"SUBSCRIBE_BUTTON_TITLE": "Únete",
		"SHARE_POST_INTRO": "Comparte:",
		"COMMENTS_INTRO": "Comentarios",
		"SITE_LICENSE": "",
		"SITE_DESCRIPTION": "Tu blog favorito :)",
		"TOC_LABEL": "Contenido",
		"PREV_ARTICLE_LABEL": "Anterior",
		"NEXT_ARTICLE_LABEL": "Siguiente",
		"ARTICLE_DATE_LABEL": "Publicado",
		"ARTICLE_LAST_UPDATED_LABEL": "Modificado por última vez",
		"ARTICLE_CATEGORY_LABEL": "Categoría",
		"ARTICLE_TAGS_LABEL": "Etiquetas",
		"SEARCH_LABEL": "Búsqueda",
		"SEARCH_DESCRIPTION": "Búsqueda en el sitio web",
		"READING_TIME_LABEL": "Tiempo estimado para leer",
		"TRANSLATIONS_INTRO": "Traducciones del artículo",
		"RECENT_ARTICLES_LABEL": "Los artículos más recientes",
	},
	"ca": {
		"SITESUBTITLE": "El teu bloc preferit",
		"COPYRIGHT": "Copyright © " + the_years[2] + " " + SITENAME + ". Tots els drets reservats.",
		"LOCALE": "ca",
		"TIMEZONE": "Europe/Madrid",
		"DEFAULT_DATE_FORMAT": "%A, %-d de %B de %Y a les %H:%M",
		"HOMEPAGE_TITLE": "Inici",
		"RELATED_POSTS_LABEL": "Articles relacionats",
		"SOCIAL_PROFILE_LABEL": "Xarxes socials",
		"PROJECTS_TITLE": "Altres projectes",
		"EMAIL_SUBSCRIPTION_LABEL": "Llista de correu, per a una comunicació més simple",
		"EMAIL_FIELD_PLACEHOLDER": "La teva adreça de correu...",
		"SUBSCRIBE_BUTTON_TITLE": "Uneix-te",
		"SHARE_POST_INTRO": "Comparteix:",
		"COMMENTS_INTRO": "Comentaris",
		"SITE_LICENSE": "",
		"SITE_DESCRIPTION": "El teu bloc favorit :)",
		"TOC_LABEL": "Contingut",
		"PREV_ARTICLE_LABEL": "Anterior",
		"NEXT_ARTICLE_LABEL": "Següent",
		"ARTICLE_DATE_LABEL": "Data de publicació",
		"ARTICLE_LAST_UPDATED_LABEL": "Data d'última modificació",
		"ARTICLE_CATEGORY_LABEL": "Categoria",
		"ARTICLE_TAGS_LABEL": "Etiquetes",
		"SEARCH_LABEL": "Cerca",
		"SEARCH_DESCRIPTION": "Cerca al lloc web",
		"READING_TIME_LABEL": "Temps estimat per llegir el text",
		"TRANSLATIONS_INTRO": "Traduccions",
		"RECENT_ARTICLES_LABEL": "Els articles més recents",
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


# category details class and dictionary

class CategoryDetails:
	name = ""
	short_description = ""
	long_description = ""

	def __init__(self, name, short_description="", desc_filename=""):
		self.name = name
		self.short_description = short_description
		desc_file_path = os.path.join(PATH, CATEGORY_DETAILS_PATH, desc_filename)
		if not desc_filename in ["", " ", None] and os.path.isfile(desc_file_path):
			with open(desc_file_path, "r", encoding="utf-8") as f:
				self.long_description = f.read()
		else:
			self.long_description = self.short_description


CATEGORY_DETAILS = {
	"Books": CategoryDetails("Books", "An awesome list of books to read and enjoy :)", "Books.txt"),
	"IT akademija/Advanced Java Programming/AJP - Modul 1. Napredno objektno programiranje": CategoryDetails("IT akademija/Advanced Java Programming/AJP - Modul 1. Napredno objektno programiranje", "Lekcije iz naprednog nivoa Java programskog jezika, ako tako mogu da kažem... :D", "ITA_AJP_1.txt"),
	"Katalonski - Català": CategoryDetails("Katalonski - Català", "Una llengua boniquíssima! :heart:"),
}
