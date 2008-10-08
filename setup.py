#! /usr/bin/env python

############################################################################
##  setup.py
##
##  Part of the DendroPy phylogenetic computation library.
##
##  Copyright 2008 Jeet Sukumaran and Mark T. Holder.
##
##  This program is free software; you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation; either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License along
##  with this program. If not, see <http://www.gnu.org/licenses/>.
##
############################################################################

"""
Package setup and installation.
"""
import ez_setup
ez_setup.use_setuptools()
from setuptools import setup
from setuptools import find_packages

import sys
import os
import subprocess

def get_dendropy_version():
    dpinit = os.path.join("dendropy", "__init__.py")
    if not os.path.exists(dpinit):
        return "#.#.#"
    else:
        dp_locals = {}
        dp_globals = {}
        execfile(dpinit, dp_globals, dp_locals)
        return dp_locals['PACKAGE_VERSION']

version = get_dendropy_version()

setup(name='DendroPy',
      version=version,     
      author='Jeet Sukumaran and Mark T. Holder',
      author_email='jeet@ku.edu and mtholder@ku.edu',
      url='http://sourceforge.net/projects/dendropy/',
      description="""\
A library for Python-based phylogenetic computation.""",
      license='GPL 3+',
      packages=['dendropy'],
      package_dir={'dendropy': 'dendropy'},
      package_data={
        "" : ['doc/*'],
        "dendropy" : ["tests/data/*"]
      },
      scripts=['scripts/sumtrees.py'],   
      test_suite = "dendropy.tests",
      include_package_data=True,         
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,      
      long_description="""\
A pure-Python library for reading, writing, simulating, manipulating and analyzing
phylogenetic trees.""",
      classifiers = [
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: GNU Library or  General Public License (GPL)",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Topic :: Scientific/Engineering :: Bio-Informatics",
            ],
      keywords='phylogenetics evolution biology',      
      )
