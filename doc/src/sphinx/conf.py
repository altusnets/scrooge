# -*- coding: utf-8 -*-
#
# Documentation config
#

import sys, os

sys.path.append(os.path.abspath('exts'))
highlight_language = 'scala'
extensions = ['sphinx.ext.extlinks', 'includecode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = []

sys.path.append(os.path.abspath('_themes'))
html_theme_path = ['_themes']
html_theme = 'flask'
html_short_title = 'Scrooge'
html_static_path = ['_static']
html_sidebars = {
   'index':    ['sidebarintro.html', 'searchbox.html'],
    '**':      ['sidebarintro.html', 'localtoc.html', 'relations.html', 'searchbox.html']
}
html_theme_options = {
  'index_logo': None
}

# These don't seem to work?
html_use_smartypants = True
html_show_sphinx = False
html_style = 'scrooge.css'

project = u'Scrooge'
description = u'A thrift code generator written in Scala'
html_logo = u'scrooge.png'
copyright = u'2013 Twitter, Inc'
version = ''
release = ''
htmlhelp_basename = "scrooge"

# e.g. :issue:`36` :ticket:`8`
extlinks = {
  'issue': ('https://github.com/twitter/scrooge/issues/%s', 'issue #')
}

rst_epilog = '''
.. include:: /links.txt
'''

pygments_style = 'flask_theme_support.FlaskyStyle'

# fall back if theme is not there
try:
    __import__('flask_theme_support')
except ImportError as e:
    print '-' * 74
    print 'Warning: Flask themes unavailable.  Building with default theme'
    print 'If you want the Flask themes, run this command and build again:'
    print
    print '  git submodule update --init'
    print '-' * 74

    pygments_style = 'tango'
    html_theme = 'default'
    html_theme_options = {}
