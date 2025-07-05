# Configuration file for the Sphinx documentation builder.
 
import os
import sys
 
# -- Path setup --------------------------------------------------------------
 
# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example:
# sys.path.insert(0, os.path.abspath('../src'))
 
# -- Project information -----------------------------------------------------
 
project = 'Bitdefender Central – Protect Your Devices'
copyright = '2025, Bitdefender'
author = 'Bitdefender Support Team'
 
# The full version, including alpha/beta/rc tags
release = '1.0.0'
 
# -- General configuration ---------------------------------------------------
 
# Add any Sphinx extension module names here, as strings.
extensions = []
 
# List of patterns, relative to source directory, that match files and directories to ignore.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
 
# -- HTML output settings ----------------------------------------------------
 
# Title shown in the browser tab and top of HTML pages
html_title = "Bitdefender Central – Complete Setup & Security Guide"
 
# Optional short title (e.g., for nav bar)
html_short_title = "Bitdefender Central"
 
# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'
 
# Choose a theme
# html_theme = 'sphinx_rtd_theme'  # Uncomment if you want to use the Read the Docs theme
 
# Hide "View page source" link
html_show_sourcelink = False
 
# Allow raw HTML blocks in .rst files
html_allow_unsafe = True
 
# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}
 
# Paths to templates and static files
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if you add CSS, JS, or images
