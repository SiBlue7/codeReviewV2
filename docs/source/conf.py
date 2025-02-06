# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Code Review'
copyright = '2025, Chevalier Enzo'
author = 'Chevalier Enzo'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('../../Functionality'))
sys.path.insert(0, os.path.abspath('../../Log'))
sys.path.insert(0, os.path.abspath('../../Report'))
sys.path.insert(0, os.path.abspath('../../Const'))

extensions = [
    'sphinx.ext.autodoc',  # Génère la doc à partir du code
    'sphinx.ext.napoleon',  # Supporte les docstrings Google et NumPy
    'myst_parser',
]

# -- Options pour autodoc ----------------------------------------------------
autodoc_default_options = {
    'members': True,         # Documente toutes les classes et fonctions
    'undoc-members': True,   # Inclut les membres sans docstrings
    'private-members': True, # Inclut les membres privés (_nom)
    'special-members': '__init__',  # Inclut les méthodes spéciales comme __init__
}

# -- Options pour Napoleon ---------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = False  # Mets à True si tu utilises NumPy style

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
