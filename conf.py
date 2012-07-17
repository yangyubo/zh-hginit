# -*- coding: utf-8 -*-



import sys, os
project = u'hginit.com 中文版'
copyright = u''
version = u''
release = u''

source_suffix = '.rst'
master_doc = 'index'
language = 'en_US'
exclude_patterns = ['_build']
extensions = ['sphinx.ext.pngmath']
pygments_style = 'sphinx'

html_title = u'hginit.com 中文版'
html_theme = 'haiku'
html_theme_path = ['../../../templates/sphinx', ]
htmlhelp_basename = 'hginit'
html_add_permalinks = None

file_insertion_enabled = False
latex_documents = [
  ('index', 'hginit.tex', u'hginit.com 中文版',
   u'', 'manual'),
]

exclude_patterns = ['README.rst']


#Add sponsorship and project information to the template context.
context = {
    'MEDIA_URL': "/media/",
    'slug': 'hginit',
    'name': u'hginit.com 中文版',
    'analytics_code': '',
}

html_context = context
