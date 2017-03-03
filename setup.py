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
from setuptools import setup

setup(name='dir_ascii',
      version='0.1',
      description='Creates an ASCII-based graphcial representation of directory hierarchies',
      url='http://github.com/tdeh/dir-ascii',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Operating System :: POSIX :: Linux',
        'Topic :: Utilities',
      ],
      keywords='tree directory hierarchy ascii',
      author='Taylor DeHaan',
      author_email='tdehaan93@gmail.com',
      license='Apache',
      packages=['dir_ascii'],
      install_requires=[
          'pytest',
          'pylint',
          'mock'
      ],
      zip_safe=False)
