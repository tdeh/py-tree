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


class DirectoryNode(object):

    def __init__(self, name):
        self._name = name
        self._child_dirs = []
        self._files = []

    def add_child(self, name):
        self._child_dirs.append(DirectoryNode(name))

    def add_file(self, filename):
        self._files.append(filename)

    def children(self):
        for node in self._child_dirs:
            yield node

    def files(self):
        for filename in self._files:
            yield filename


class DirectoryTree(object):

    def __init__(self, root_name):
        self._root = DirectoryNode(root_name)

    def get_root(self):
        return self._root

