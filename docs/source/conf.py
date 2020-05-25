# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('./../../src/'))
sys.path.insert(0, os.path.abspath('./../../src/musictheory'))
# directory relative to this conf file
CURDIR = os.path.abspath(os.path.dirname(__file__))
# add custom extensions directory to python path
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), 'extensions'))


# -- Project information -----------------------------------------------------

project = 'musictheory'
copyright = '2020, Fabian C. Moss'
author = 'Fabian C. Moss'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc', 
    'sphinx.ext.coverage', 
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx'
    # 'sphinxcontrib.lilypond'
    # 'sphinxcontrib.bibtex'
]

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# # configures bibliography
# # see http://wnielson.bitbucket.org/projects/sphinx-natbib/
# natbib = {
#     'file': os.path.join(CURDIR,'references.bib'),
#     'brackets': '{}',
#     'separator': ',',
#     'style': 'numbers',
#     'sort': True,
# }

# pnglily_fontsize = ['6', '-3'] # The first value is for 'lily' role setting in absolute fontsize. 
# The second value is for 'lily' directive setting in relative fontsize.

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"
html_theme_options = {
    # 'github_user': 'fabianmoss',
    # 'github_repo': 'musictheory',
    "logo": "logo2.png"
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# link to master doc
master_doc = 'index'