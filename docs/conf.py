# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from typing import Any, Dict

# add the demo python code to the path, so that it can be used to demonstrate
# source links
sys.path.append(os.path.abspath("./kitchen-sink/demo_py"))

# -- Project information -----------------------------------------------------
#

html_title = full_title = project = "Daniele Procida"
copyright = "2022, Daniele Procida"
author = "Daniele Procida"

# -- General configuration ---------------------------------------------------
#

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # Our custom extension, only meant for Furo's own documentation.
    "furo.sphinxext",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",
]
templates_path = ["_templates"]

# -- Options for extlinks ----------------------------------------------------
#

extlinks = {
    "pypi": ("https://pypi.org/project/%s/", ""),
}

# -- Options for intersphinx -------------------------------------------------
#

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# -- Options for TODOs -------------------------------------------------------
#

todo_include_todos = True


# -- Options for HTML output -------------------------------------------------
#

html_theme = "furo"
html_title = full_title = project = "Daniele Procida"
language = "en"

html_static_path = ["_static"]
html_css_files = ["pied-piper-admonition.css"]

html_permalinks_icon = "¶"

html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ]
}

html_theme_options: Dict[str, Any] = {
    "sidebar_hide_name": True,
    "top_of_page_button": None,
}


# -- Options for theme development -------------------------------------------
# Make sure these are all set to the default values.

html_js_files = []
html_context: Dict[str, Any] = {}
# html_show_sphinx = False
# html_show_copyright = False
# html_last_updated_fmt = ""
