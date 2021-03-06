# -*- coding: utf-8 -*-
#
# CanberrraUAV Administrivia documentation build configuration file, created by
# sphinx-quickstart on Mon Feb 25 21:28:16 2013.
#

import sys, os


# -- General configuration -----------------------------------------------------
extensions = ['sphinx.ext.todo',]# 'sphinxcontrib.spelling' <--problematic

spelling_lang='en_AU'
spelling_word_list_filename='OK_wordlist.txt'
spelling_show_suggestions=True

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'CanberraUAV Public'
copyright = u'2013, CanberraUAV'

#version = '1.0'
#release = '1.0'
exclude_trees = ['_build']
pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------
html_theme = 'haiku'
#html_theme_options = {
#    "nosidebar": "true"
#}
html_static_path = ['_static']
htmlhelp_basename = 'CanberraUAVAdministriviadoc'

# -- Options for LaTeX output --------------------------------------------------
latex_documents = [
  ('index', 'CanberraUAVAdministrivia.tex', u'CanberraUAV Administrivia Documentation',
   u'CanberraUAV Team', 'manual'),
]


# Reverse toctree hack, so that we can have most recent meeting minutes first
# to use this, add ":reversed:" parameter to toctree directives.
from sphinx.directives import TocTree
from docutils.parsers.rst import directives

class NewTocTree(TocTree):
    option_spec = dict(TocTree.option_spec,
                       reversed=directives.flag)

    def run(self):
        rst = super(NewTocTree, self).run()
        if 'reversed' in self.options:
            rst[0][0]['entries'].reverse()
        return rst

def setup(app):
    app.add_directive('toctree', NewTocTree)

