Sphinx Ref Helper
#################

.. image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

This plugin works with Sublime Text 3. It searches the first open folder
in any given Sublime Text 3 window for Sphinx internal doc references labels.
It displays each one it finds (along with the file it was found in) in the
quick panel. If you select one (either by clicking or hitting enter) it will
insert the correct ``:ref:```` in the document you are editing at the current
cursor location. Note that this plugin stands alone and does not require
Sphinx to be installed or the documenation to have been built.

.. image:: images/sphinx-ref-help-screenshot.png

I recommend having just one Sphinx documentation project folder open in any
given window.

How to use it
=============

#.  Open a Sphinx project using “Open Folder." If there is a conf.py,
    the plugin tries to check if there are "exclude patterns" to avoid.
#.  Put cursor where you want to insert ``:ref:````.
#.  Type (``primary + 1`` - "ctrl key" in Windows/Linux and "⌘ key"
    in MacOS).
#.  Select ref from the list to insert at current cursor location.

Manual installation
===================

#. Open Sublime Text 3.
#. Go to “Preferences” and click “Browse Packages.”
#. Double click on the “User” directory.
#. Drop both files in the “User” directory.

Limitations
===========

This plugin was created to help me work with Sphinx documentation projects
that I might not already be familiar with. As such, it is meant for
convenience and is a work in progress.

* Try to open folders that contain just the Sphinx project. Opening the root
  directory of your system would be a bad idea and will probably hang Sublime
  Text. Don't try it, please.
* Multiple folders open in the same window are going to be a problem, as the
  plugin is coded to look at only the first folder. It works for me, but it
  might not work for you. It seems to me that sharing refs between projects
  would probably be confusing anyway. 
* I put in some code to strip out http link refs. However, if your links split
  lines, they're going to show up in the list. Since many of these are only
  available from within the file in which they were created, be careful.
* There are probably things that I missed. Feel free to help out.