#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2015 Jérémie DECOCK (http://www.jdhp.org)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
A markdown file viewer.

WARNING: Debian users have to install the "python3-markdown" package to run
         this snippet.

WARNING: Debian users have to install the "libwebkitgtk-3.0-dev" package to run
         this snippet.

SEE: /usr/share/doc/python-markdown-doc/docs/index.html ("python-markdown-doc" Debian package)
"""

import gi
gi.require_version('WebKit', '3.0')

from gi.repository import Gtk as gtk
from gi.repository import WebKit as webkit

import markdown

import argparse

def md_to_html(markdown_filename, output_format="html5"):
    """
    Convert the "markdown_filename" file to HTML.
    
    "output_format" can be:
    - "xhtml1": Outputs XHTML 1.x. Default.
    - "xhtml5": Outputs XHTML style tags of HTML 5
    - "xhtml": Outputs latest supported version of XHTML (currently XHTML 1.1).
    - "html4": Outputs HTML 4
    - "html5": Outputs HTML style tags of HTML 5
    - "html": Outputs latest supported version of HTML (currently HTML 4).
    """

    md_string = ""
    with open(markdown_filename, "r") as fd:
        md_string = fd.read()

    html = markdown.markdown(text=md_string, output_format=output_format)

    return html

def main():

    # parse options
    parser = argparse.ArgumentParser(description='A markdown file viewer.')
    parser.add_argument('filename', nargs=1, metavar='STRING', help='the markdown file to display')
    args = parser.parse_args()

    md_filename = args.filename[0]

    # markdown to html
    html = md_to_html(md_filename)

    # make the Gtk window
    window = gtk.Window()
    window.maximize()

    # make the webkit widget
    webview = webkit.WebView()
    webview.load_html_string(html, '')

    # scrolled window
    scrolled_window = gtk.ScrolledWindow()
    scrolled_window.set_policy(gtk.PolicyType.AUTOMATIC, gtk.PolicyType.AUTOMATIC)  # should be gtk.PolicyType.AUTOMATIC, gtk.PolicyType.ALWAYS or gtk.PolicyType.NEVER
    scrolled_window.add(webview)

    window.add(scrolled_window)

    # main
    window.connect("delete-event", gtk.main_quit) # ask to quit the application when the close button is clicked
    window.show_all()                             # display the window
    gtk.main()                                    # GTK+ main loop

if __name__ == '__main__':
    main()

