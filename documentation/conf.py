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


import concurrent.futures
import os
import shutil
import subprocess
import venv


def remove(path: str):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    except IsADirectoryError:
        shutil.rmtree(path)


def setup_venv():
    envelope_builder = venv.EnvBuilder(system_site_packages=False, with_pip=True)
    envelope_builder.create(VENV_PATH)


def install_package(package_name: str):
    subprocess.call([PIP_PATH, "install", package_name])


def install_package_tuple(package_tuple: tuple[str, ...]):
    thread_pool = concurrent.futures.ThreadPoolExecutor()
    for package in package_tuple:
        thread_pool.submit(lambda: install_package(package))
    thread_pool.shutdown(wait=True)


def create_api_documentation():
    remove(API_DOCUMENTATION_PATH)
    subprocess.call(
        [
            SPHINX_APIDOC_PATH,
            "--tocfile",
            API_DOCUMENTATION_TREE_NAME,
            "-M",
            "-d",
            "1",
            "-o",
            API_DOCUMENTATION_PATH,
            MUTWO_PATH,
        ]
    )


SPHINX_VERSION = "4.5.0"

VENV_PATH = "virtualenv"
BIN_PATH = f"{VENV_PATH}/bin"
PIP_PATH = f"{BIN_PATH}/pip3"
SPHINX_APIDOC_PATH = f"{BIN_PATH}/sphinx-apidoc"
SPHINX_BUILD_PATH = f"{BIN_PATH}/sphinx-build"
MUTWO_PATH = f"{VENV_PATH}/lib/python3.9/site-packages/mutwo"

DOCUMENTATION_PATH = "."
SPHINX_OUTPUT_PATH = "{DOCUMENTATION_PATH}/_build"
API_DOCUMENTATION_PATH = f"{DOCUMENTATION_PATH}/api"
API_DOCUMENTATION_TREE_NAME = "api_documentation"

MUTWO_PACKAGE_TUPLE = ("mutwo.ext-core", "mutwo.ext-music")

SPHINX_PACKAGE_TUPLE = (
    f"sphinx=={SPHINX_VERSION}",
    "sphinx-autodoc-annotation==1.0-1",
    "autodocsumm==0.2.4",
    "insipid-sphinx-theme==0.2.8",
)

setup_venv()
install_package_tuple(MUTWO_PACKAGE_TUPLE + SPHINX_PACKAGE_TUPLE)
create_api_documentation()

sys.path.insert(0, os.path.abspath("../."))
sys.path.append(os.path.abspath("./virtualenv/lib/python3.9/site-packages/mutwo"))


# -- Project information -----------------------------------------------------

project = "mutwo"
copyright = "2022, Levin Eric Zimmermann, Tim Pauli"
author = "Levin Eric Zimmermann, Tim Pauli"

# The full version, including alpha/beta/rc tags
release = "2022"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "autodocsumm",
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
autodoc_default_options = {
    # "ignore-module-all": True,
    "autosummary": True,
}
add_module_names = False


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_permalinks_icon = '§'
html_theme = 'insipid'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
