# -*- coding: utf-8 -*-
"""
    jinja2
    ~~~~~~

    Jinja2 is a template engine written in pure Python.  It provides a
    Django inspired non-XML syntax but supports inline expressions and
    an optional sandboxed environment.

    Nutshell
    --------

    Here a small example of a Jinja2 template::

        {% extends 'base.html' %}
        {% block title %}Memberlist{% endblock %}
        {% block content %}
          <ul>
          {% for user in users %}
            <li><a href="{{ user.url }}">{{ user.username }}</a></li>
          {% endfor %}
          </ul>
        {% endblock %}


    :copyright: 2008 by Armin Ronacher, Christoph Hack.
    :license: BSD, see LICENSE for more details.
"""
__docformat__ = 'restructuredtext en'
try:
    __version__ = __import__('pkg_resources') \
        .get_distribution('Jinja2').version
except:
    __version__ = 'unknown'

# high level interface
from jinja2.environment import Environment, Template

# loaders
from jinja2.loaders import BaseLoader, FileSystemLoader, PackageLoader, \
     DictLoader, FunctionLoader, PrefixLoader, ChoiceLoader

# undefined types
from jinja2.runtime import Undefined, DebugUndefined, StrictUndefined

# decorators and public utilities
from jinja2.filters import environmentfilter, contextfilter
from jinja2.utils import Markup, escape, environmentfunction, contextfunction