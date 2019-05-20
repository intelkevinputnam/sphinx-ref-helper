Sphinx Ref Helper
#################

This plugin works with Sublime Text 3. It searches the folder for reference
labels and lists them in a quick panel. If you select one it will insert
the correct ``:ref:```` in the document you are editing. The documentation
does not have to have been built for this work.

This is very much a work in progress. 

Installation
============

#. Open Sublime Text 3.
#. Go to “Preferences” and click “Browse Packages.”
#. Double click on the “User” directory.
#. Drop both files in the “User” directory.

Usage
=====

#.  Open a Sphinx project using “Open Folder." Make sure the conf.py
    is in the top level directory. It's OK if there isn't one, but
    the plugin tries to check if there are "exclude patterns."
#.  Put cursor where you want to insert ``:ref:````
#.  Type (``primary + 1`` - ctrl in Windows/Linux and "apple key" in MacOS)
#.  Select ref from the list to insert at current cursor location.
