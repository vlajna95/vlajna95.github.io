import os
import os.path
import logging
from pelican.contents import Page
from pelican import signals

log = logging.getLogger(__name__)


"""
def get_categories(generator, metadata):
	categories = text_type(metadata.get("category")).split(",")
	metadata["categories"] = [Category(name, generator.settings) for name in categories]
	metadata["category"] = metadata["categories"][0]

def create_categories(generator):
	generator.categories = []
	cat_dct = defaultdict(list)
	for article in generator.articles:
		for cat in {a for c in article.categories for a in c.ancestors}:
			cat_dct[cat].append(article)
	generator.categories = sorted(list(cat_dct.items()), reverse=generator.settings.get("REVERSE_CATEGORY_ORDER") or False)
	generator._update_context(["categories"])

	# Add descendents and children
	descendents = defaultdict(list)
	children = defaultdict(list)
	for category, articles in generator.categories:
		for anc in category.ancestors[:-1]:
			descendents[anc].append(category)
		if category.parent:
			children[category.parent].append(category)
	for category, articles in generator.categories:
		category.descendents = sorted(descendents[category])
		category.children = sorted(children[category])

def register():
	signals.article_generator_context.connect(get_categories)
	signals.article_generator_finalized.connect(create_categories)
"""


def yield_files(root):
	root = os.path.realpath(os.path.abspath(root))
	for dirpath, dirnames, filenames in os.walk(root):
		for dirname in list(dirnames):
			try:
				if dirname.startswith("."):
					dirnames.remove(dirname)
			except IndexError:
				# duplicate already removed?
				pass
		for filename in filenames:
			if filename.startswith("."):
				continue
			yield os.path.join(dirpath, filename)

def make_page(readers, context, filename):
	base_path, filename = os.path.split(filename)
	page = readers.read_file(base_path, filename, Page, None, context)
	slug, _ = os.path.splitext(filename)
	return slug, page

def make_pages(readers, context, path):
	pages = {}
	for filename in yield_files(path):
		try:
			slug, page = make_page(readers, context, filename)
			log.debug(f"Page for category {slug} created successfully.")
		except Exception:
			log.exception("Could not make autopage for %r", filename)
			continue
		pages[slug] = page
	return pages

def create_autopages(article_generator, metadata):
	settings = article_generator.settings
	readers = article_generator.readers
	context = article_generator.context
	authors_path = settings.get("AUTHOR_PAGE_PATH", "authors")
	categories_path = settings.get("CATEGORY_PAGE_PATH", "categories")
	tags_path = settings.get("TAG_PAGE_PATH", "tags")
	author_pages = make_pages(readers, context, authors_path)
	category_pages = make_pages(readers, context, categories_path)
	tag_pages = make_pages(readers, context, tags_path)
	for author, _ in article_generator.authors:
		author.page = author_pages.get(author.slug, "")
	for category, _ in article_generator.categories:
		category.page = category_pages.get(category.slug, "")
	for tag in article_generator.tags:
		tag.page = tag_pages.get(tag.slug, "")

def register():
	log.debug("index_pages loaded")
	signals.article_generator_context.connect(create_autopages)


"""
def test(generator, metadata):
	log.debug(f"generator: {generator}")
	log.debug(f"metadata: {metadata}")
	root = os.getcwd()
	root = os.path.realpath(os.path.abspath(root))
	for dirpath, dirnames, filenames in os.walk(root):
		for dirname in list(dirnames):
			try:
				if dirname.startswith("."):
					dirnames.remove(dirname)
			except IndexError:
				# duplicate already removed?
				pass
		for filename in filenames:
			if filename.startswith("."):
				continue
			log.debug(f"{filename} found")

def register():
	signals.article_generator_context.connect(test)
"""
