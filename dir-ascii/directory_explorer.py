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

from collections import deque
import os
import re


class DirectoryExplorer(object):

    def __init__(self, start_dir=".", show_hidden=False, recursion_limit=10):
        self._start_dir = start_dir
        self._show_hidden = show_hidden
        self._recursion_limit = recursion_limit

    def _sort_and_filter(self, raw_list, root):
        files = []
        directories = []

        for entry in raw_list:
            if not self._show_hidden and re.match(r"\..*", entry):
                continue

            print entry
            if os.path.isfile(os.path.join(root, entry)):
                print "file"
                files.append(entry)
            else:
                print "dir"
                directories.append(entry)

        return files, directories

    def explore(self):
        results = []
        recursion_level = 0
        current_level = deque(self._start_dir)
        next_level = deque()

        while len(current_level) != 0:
            current_dir = current_level.popleft()

            listdir_result = os.listdir(current_dir)
            files, directories = self._sort_and_filter(listdir_result,
                                                       current_dir)
            results.append((directories, files))

            if recursion_level == self._recursion_limit:
                continue

            for directory in directories:
                next_level.append(os.path.join(current_dir, directory))

            if len(current_level) == 0 and \
                    recursion_level < self._recursion_limit:
                current_level = next_level
                next_level = deque()
                recursion_level += 1

        return results
