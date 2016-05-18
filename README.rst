==================
`Markdown Viewer`_
==================

Copyright (c) 2015 Jeremie DECOCK (http://www.jdhp.org)


* Web site: http://www.jdhp.org/projects_en.html#markdown-viewer
* Source code: https://github.com/jeremiedecock/markdown-viewer
* Issue tracker: https://github.com/jeremiedecock/markdown-viewer/issues
* Markdown Viewer on PyPI: https://pypi.python.org/pypi/markdown-viewer


Description
===========

`Markdown Viewer`_ is an open source lightweight Python tool to display
Markdown files.

Note:

    This project is in beta stage.


Dependencies
============

- Python >= 3.0
- GTK+3 with Python 3 bindings
- Webkit for GTK+3
- Markdown for Python 3


.. _install:

Installation
============

Gnu/Linux
---------

You can install, upgrade, uninstall Markdown Viewer with these commands (in a
terminal)::

    pip install --pre markdown-viewer
    pip install --upgrade markdown-viewer
    pip uninstall markdown-viewer

Or, if you have downloaded the Markdown Viewer source code::

    python3 setup.py install

.. There's also a package for Debian/Ubuntu::
.. 
..     sudo apt-get install markdown-viewer

Windows
-------

.. Note:
.. 
..     The following installation procedure has been tested to work with Python
..     3.4 under Windows 7.
..     It should also work with recent Windows systems.

You can install, upgrade, uninstall Markdown Viewer with these commands (in a
`command prompt`_)::

    py -m pip install --pre markdown-viewer
    py -m pip install --upgrade markdown-viewer
    py -m pip uninstall markdown-viewer

Or, if you have downloaded the Markdown Viewer source code::

    py setup.py install

MacOSX
-------

Note:

    The following installation procedure has been tested to work with Python
    3.5 under MacOSX 10.9 (*Mavericks*).
    It should also work with more recent MacOSX systems.

You can install, upgrade, uninstall Markdown Viewer with these commands (in a
terminal)::

    pip install --pre markdown-viewer
    pip install --upgrade markdown-viewer
    pip uninstall markdown-viewer

Or, if you have downloaded the Markdown Viewer source code::

    python3 setup.py install

Markdown Viewer requires GTK+3 and its Python 3 bindings plus few additional
libraries to run.
These dependencies can be installed using MacPorts::

    port install gtk3
    port install py35-gobject3
    port install webkit-gtk3
    port install py35-markdown

.. or with Hombrew::
.. 
..     brew install gtk+3
..     brew install pygobject3


Bug reports
===========

To search for bugs or report them, please use the Markdown Viewer Bug Tracker at:

    https://github.com/jeremiedecock/markdown-viewer/issues


License
=======

This project is provided under the terms and conditions of the
`MIT License`_.


.. _MIT License: http://opensource.org/licenses/MIT

.. _Markdown Viewer: http://www.jdhp.org/projects_en.html#markdown-viewer
