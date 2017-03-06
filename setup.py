# Copyright 2017 Taylor DeHaan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

setup(name='py-tree',
      version='1.0.1',
      description='A command line tool for generating text-based graphcial representation of file hierarchies.',
      url='http://github.com/tdeh/py-tree',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
        'Topic :: Utilities',
      ],
      keywords='tree directory files hierarchy',
      author='Taylor DeHaan',
      author_email='tdehaan93@gmail.com',
      license='Apache',
      packages=['py_tree'],
      test_suite='nose.collector',
      tests_require=[
          'nose',
          'mock'
      ],
      entry_points={
          'console_scripts': ['py-tree=py_tree.command_line:command_line_runner'],
      },
      zip_safe=False)
