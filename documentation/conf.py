# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

sys.path.insert(0, os.path.abspath("../."))
sys.path.append(os.path.abspath("./"))


# -- Project information -----------------------------------------------------

project = "mutwo"
copyright = "2023, mutwo authors"
author = "Levin Eric Zimmermann, Tim Pauli"
language = "en"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "autoclasstoc",
    "sphinx.ext.autodoc",
    # "autodocsumm",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.inheritance_diagram",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# autodoc settings
autosummary_generate = False
autosummary_generate_overwrite = False
autodoc_typehints = "description"
autodoc_member_order = "groupwise"
add_module_names = False

autodoc_default_options = {
    "ignore-module-all": False,
    "autosummary": True,
    "members": True,
    "special-members": False,
    "private-members": False,
    "inherited-members": False,
    "undoc-members": False,
    "exclude-members": "__weakref__",
    "show-inheritance": True,
}


autoclasstoc_sections = [
    "public-attrs",
    "public-methods-without-dunders",
    # "private-attrs",
    # "private-methods",
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "classic"

html_css_files = ["custom.css"]

# html_permalinks_icon = "§"
linkcolor = "dimgray"
html_theme_options = {
    "body_max_width": "none",
    "sidebarbgcolor": "white",
    "sidebartextcolor": "black",
    "sidebarlinkcolor": linkcolor,
    "visitedlinkcolor": linkcolor,
    "headbgcolor": "white",
    "headtextcolor": "black",
    "linkcolor": linkcolor,
    "visitedlinkcolor": linkcolor,
    "footerbgcolor": "white",
    "footertextcolor": "black",
    "relbarbgcolor": "white",
    "relbartextcolor": "black",
    "relbarlinkcolor": linkcolor,
    "codebgcolor": "WhiteSmoke",
}


html_sidebars = {
    "**": ["searchbox.html"],
    "using/windows": ["windowssidebar.html", "searchbox.html"],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_show_sphinx = False
