# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Source2Blender"
copyright = "2023, Espion"
author = "Espion"

release = "0.1"
version = "0.1.0"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",

]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

# html_theme = "sphinx_rtd_theme"
html_theme = "furo"

html_static_path = ['_static']

# html_logo = "s2b.png"

html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

# -- Options for EPUB output
epub_show_urls = "footnote"

# -- Used for allowing cross-referencing, added as solution from: https://stackoverflow.com/questions/15394347/adding-a-cross-reference-to-a-subheading-or-anchor-in-another-page
extensions = [
    'sphinx.ext.autosectionlabel'
]
autosectionlabel_prefix_document = True


def setup(app):
    app.add_css_file("css/rtd_dark.css")
