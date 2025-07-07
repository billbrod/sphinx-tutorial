# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinx-tutorial'
copyright = '2025, Billy Broderick'
author = 'Billy Broderick'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # latexsyntax for math
    "sphinx.ext.mathjax",
    # docstrings
    "sphinx.ext.napoleon",
    "numpydoc",
    # matplotlib in your docs
    "matplotlib.sphinxext.plot_directive",
    "matplotlib.sphinxext.mathmpl",
    # build API documentation
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinxcontrib.apidoc",
    # link to other sphinx projects (and maybe your own?)
    "sphinx.ext.intersphinx",
    # copy code easily
    "sphinx_copybutton",
    # markdown and text-based notebooks
    "myst_nb",
    # bibtex supports
    "sphinxcontrib.bibtex",
    # little button to view code
    "sphinx.ext.viewcode",
]
templates_path = ['_templates']
exclude_patterns = []

intersphinx_mapping = {
    "numpy": ("https://numpy.org/doc/stable/", None),
}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# Napoleon settings
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = False

numfig = True

# SPHINX CROSS REFERENCES

add_function_parentheses = False

# MYST

myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "amsmath",
]

# SPHINXCONTRIB-BIBTEX
bibtex_bibfiles = ["references.bib"]
bibtex_reference_style = "author_year"

# APIDOC
apidoc_module_dir = "../../src/my_cool_package"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

# Additional theme options
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/billbrod/sphinx-tutorial/",
            "icon": "fab fa-github",
            "type": "fontawesome",
        },
    ],
    "show_prev_next": True,
}

# SPHINX COPYBUTTON
copybutton_exclude = ".linenos, .gp, .go"


nb_execution_raise_on_error = True
