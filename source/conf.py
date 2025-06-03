
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Biophotonics Server Guide'
author = 'Biophotonics Group'
release = '1.0'

extensions = [
    'myst_parser',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    "navigation_depth": 2,  # only show up to h2 / second-level headers
}