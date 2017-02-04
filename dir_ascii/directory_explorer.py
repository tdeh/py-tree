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
    """
    This class exposes an explore() method which performs a breadth-first search
    through directories and returns the results. The invoker can specify whether
    hidden files and directories are displayed (".[name]") and can set a maximum
    recursion level.
    """

    def __init__(self, start_dir=".", show_hidden=False, recursion_limit=10):
        self._start_dir = start_dir
        self._show_hidden = show_hidden
        self._recursion_limit = recursion_limit

    def _sort_and_filter(self, raw_list, root):
        """
        Takes a list of directories and files, parses each entry sorting it
        based on whether it's a file or a directory, filters out hidden files if
        show_hidden is False, and returns a tuple of file and directory lists.

        @param raw_list List containing string directory and file names
        @param root Root path to the entries in the list
        @return A tuple of two lists, one for files and the other for
                directories
        """
        # Initialize lists for files and directories
        files = []
        directories = []

        # Iterate through each entry in the file/directory list
        for entry in raw_list:
            # If show hidden is false and the entry starts with a '.', continue
            # to the next entry
            if not self._show_hidden and re.match(r"\..*", entry):
                continue

            # If the entry is a file, append it to the file list, else append
            # it to the directory list
            if os.path.isfile(os.path.join(root, entry)):
                files.append(entry)
            else:
                directories.append(entry)

        # Return tuple of the file and directory list
        return files, directories

    def explore(self):
        results = []
        recursion_level = 0
        current_level = deque()
        next_level = deque()

        current_level.append(self._start_dir)
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
