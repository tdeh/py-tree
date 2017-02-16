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

"""This module contains the DirectoryExplorer class.

The DirectoryExplorer class is used to recursively explore files and
directories.
"""

from collections import deque
import os
import re
from .directory_tree import DirectoryTree


class DirectoryExplorer(object):
    """Recursively explores files and directories.

    This class exposes an explore() method which performs a breadth-first search
    through directories and returns the results. The invoker can specify whether
    hidden files and directories are displayed and can set a maximum recursion
    level.

    Args:
        start_dir (str): The path to the directory where the BFS will originate.
        show_hidden (bool): When false, filter out hidden files and directories.
            Hidden files and directories start with a "."
        recursion_limit (int): The number of recursion levels that can should be
            explored.

    Attributes:
        _start_dir (str): The path to the directory where the BFS will
            originate.
        _show_hidden (bool): When false, filter out hidden files and
            directories.
        _recursion_limit (int): The number of recursion levels that will be
            explored.
    """

    def __init__(self, start_dir=".", show_hidden=False, recursion_limit=10):
        self._start_dir = start_dir
        self._show_hidden = show_hidden
        self._recursion_limit = recursion_limit

    def _sort_and_filter(self, raw_list, root):
        """Sorts and filters a list of files and directories.

        Takes a list of directories and files, parses each entry sorting it
        based on whether it's a file or a directory, filters out hidden files if
        show_hidden is False, and returns a tuple of file and directory lists.

        Args:
            raw_list (list): List containing string directory and file names.
            root (str): Root path to the entries in the list.

        Returns:
            A tuple of two lists, one for files and the other for directories.
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
        """Performs a breadth-first search on directory contents.

        The search starts from from the _start_dir and will continue until
        either there are no more directories to explore or the recursion limit
        has been met.

        Returns:
            A list of tuples. The tuples consist of two lists; the first
            containing directories and the second containing files. Each entry
            in the list represents the contents of a directory.
        """
        # Initialize results and recursion_level variables
        results = []
        recursion_level = 0

        # Initialize the two queues for the current level and the next level
        current_level = deque()
        next_level = deque()

        # Add the start directory to the current level
        current_level.append(self._start_dir)

        # Loop while the current level queue is not empty
        while len(current_level) != 0:
            # Pop the current directory from the top of the queue
            current_dir = current_level.popleft()

            # Use os.listdir to get a list of all files & directories inside of
            # the current_dir
            listdir_result = os.listdir(current_dir)

            # Sort and filter the results from listdir
            files, directories = self._sort_and_filter(listdir_result,
                                                       current_dir)

            # Add a tuple of the sorted directories and files to the results
            results.append((directories, files))

            # If the recursion level is at the limit, continue
            if recursion_level == self._recursion_limit:
                continue

            # For each directory inside of current_dir, add the absolute path
            # to the next level queue
            for directory in directories:
                next_level.append(os.path.join(current_dir, directory))

            # If the current levl queue is empty and we are still below the
            # recursion limit, set the current level queue equal to the next
            # level queue and increment the recursion level
            if len(current_level) == 0 and \
                    recursion_level < self._recursion_limit:
                current_level = next_level
                next_level = deque()
                recursion_level += 1

        return results

    def build_tree(self):
        """Builds a DirectoryTree by BFSing through directory contents.

        This method is very similar to explore() except that this method builds
        and returns a DirectoryTree object instead of alist of tuples.

        Returns:
            A DirectoryTree object.
        """
        # Initialize result and recursion_level variables
        result = DirectoryTree(self._start_dir)
        recursion_level = 0

        # Initialize the two queues for the current level and the next level
        current_level = deque()
        next_level = deque()

        # Add the start directory and root to the current level
        current_level.append((self._start_dir, result.get_root()))

        # Loop while the current level queue is not empty
        while len(current_level) != 0:
            # Pop the current directory and node from the top of the queue
            current_dir, current_node = current_level.popleft()

            # Use os.listdir to get a list of all files & directories inside of
            # the current_dir
            listdir_result = os.listdir(current_dir)

            # Sort and filter the results from listdir
            files, directories = self._sort_and_filter(listdir_result,
                                                       current_dir)

            # Add files to node
            current_node.add_files(files)

            # For each directory inside of current_dir, add child node
            for directory in directories:
                current_node.add_child(directory)

                # Append dirname + node tuple to next level queue if recursion
                # limit has not been reached
                if recursion_level != self._recursion_limit:
                    next_level.append((os.path.join(current_dir, directory),
                                       current_node.get_last_child()))

            # If the current levl queue is empty and we are still below the
            # recursion limit, set the current level queue equal to the next
            # level queue and increment the recursion level
            if len(current_level) == 0 and \
                    recursion_level < self._recursion_limit:
                current_level = next_level
                next_level = deque()
                recursion_level += 1

        return result
