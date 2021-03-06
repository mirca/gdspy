######################################################################
#                                                                    #
#  Copyright 2009-2016 Lucas Heitzmann Gabrielli                     #
#                                                                    #
#  This file is part of gdspy.                                       #
#                                                                    #
#  gdspy is free software: you can redistribute it and/or modify it  #
#  under the terms of the GNU General Public License as published    #
#  by the Free Software Foundation, either version 3 of the          #
#  License, or any later version.                                    #
#                                                                    #
#  gdspy is distributed in the hope that it will be useful, but      #
#  WITHOUT ANY WARRANTY; without even the implied warranty of        #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the     #
#  GNU General Public License for more details.                      #
#                                                                    #
#  You should have received a copy of the GNU General Public         #
#  License along with gdspy.  If not, see                            #
#  <http://www.gnu.org/licenses/>.                                   #
#                                                                    #
######################################################################

from setuptools import setup, Extension

with open('README.md') as fin:
    long_description = fin.read()

setup(
    name='gdspy',
    version='1.0',
    author='Lucas Heitzmann Gabrielli',
    author_email='heitzmann@gmail.com',
    license='GNU General Public License v3 (GPLv3)',
    url='https://github.com/heitzmann/gdspy',
    description='Python module for creating/importing/merging GDSII files.',
    long_description=long_description,
    keywords='GDSII CAD layout',
    packages=['gdspy'],
    package_dir={'gdspy': 'gdspy'},
    package_data={'gdspy': ['data/*']},
    ext_modules=[
        Extension('gdspy.boolext', ['gdspy/boolext.c']),
        Extension('gdspy.clipper', ['gdspy/clipper.cpp'])
    ],
    provides=['gdspy'],
    requires=['numpy'],
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: C',
        'Programming Language :: C++',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)'
    ],
    use_2to3=True,
    zip_safe=False,
)
