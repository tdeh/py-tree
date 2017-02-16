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

"""This modules contains tests for the DirectoryExplorer class.

Example:
    These tests can be run with the command::

        $ python -m dir_ascii.tests.test_directory_explorer
"""

import os
import shutil
import unittest
from ..directory_explorer import DirectoryExplorer


class TestDirectoryExplorer(unittest.TestCase):
    """Unittest class containing tests for DirectoryExplorer."""

    def setUp(self):
        self.test_dir = os.path.abspath("./test_dir/") + "/"
        os.mkdir(self.test_dir)

        self.hidden_files = [".hidfile.txt", "..hidfile.txt"]
        self.hidden_dirs = [".hiddir", "..hiddir"]

        for fname in self.hidden_files:
            open(self.test_dir + fname, 'a').close()

        for dir_name in self.hidden_dirs:
            os.mkdir(self.test_dir + dir_name)

        self.dir_pattern_a = "dira%i"
        self.dir_pattern_b = "dirb%i"
        self.file_pattern_a = "filea%i.txt"
        self.file_pattern_b = "fileb%i.txt"

        path = self.test_dir
        for i in range(3):
            os.mkdir(path + (self.dir_pattern_a % i))
            os.mkdir(path + (self.dir_pattern_b % i))
            path = os.path.join(path, self.dir_pattern_a % i) + "/"
            open(path + (self.file_pattern_a % i), 'a').close()
            open(path + (self.file_pattern_b % i), 'a').close()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_explore_hides_hidden_files(self):
        """Tests that show_hidden=false will not show hidden files."""
        direxp = DirectoryExplorer(start_dir=self.test_dir, show_hidden=False)
        results = direxp.explore()
        _, files = results[0]

        for fname in self.hidden_files:
            self.assertFalse(fname in files)

    def test_explore_hides_hidden_dirs(self):
        """Tests that show_hidden=false will not show hidden directories."""
        direxp = DirectoryExplorer(start_dir=self.test_dir, show_hidden=False)
        results = direxp.explore()
        dirs, _ = results[0]

        for dir_name in self.hidden_dirs:
            self.assertFalse(dir_name in dirs)

    def test_explore_shows_hidden_files(self):
        """Tests that show_hidden=true will show hidden files."""
        direxp = DirectoryExplorer(start_dir=self.test_dir, show_hidden=True)
        results = direxp.explore()
        _, files = results[0]

        for fname in self.hidden_files:
            self.assertTrue(fname in files)

    def test_explore_shows_hidden_dirs(self):
        """Tests that show_hidden=true will show hidden directories."""
        direxp = DirectoryExplorer(start_dir=self.test_dir, show_hidden=True)
        results = direxp.explore()
        dirs, _ = results[0]

        for dir_name in self.hidden_dirs:
            self.assertTrue(dir_name in dirs)

    def test_explore_finds_all_files(self):
        """Test that explore will find all files."""
        direxp = DirectoryExplorer(start_dir=self.test_dir, show_hidden=False)
        results = direxp.explore()

        recursion_level = 0
        for _, files in results:
            if files:
                self.assertTrue(self.file_pattern_a % recursion_level in files)
                self.assertTrue(self.file_pattern_b % recursion_level in files)
                recursion_level += 1

    def test_explore_finds_all_dirs(self):
        """Test that explore will find all directories."""
        direxp = DirectoryExplorer(start_dir=self.test_dir, show_hidden=False)
        results = direxp.explore()

        recursion_level = 0
        for dirs, _ in results:
            if dirs:
                self.assertTrue(self.dir_pattern_a % recursion_level in dirs)
                self.assertTrue(self.dir_pattern_b % recursion_level in dirs)
                recursion_level += 1

    def test_recursion_limit(self):
        """Test that explore exits once meeting the recursion limit."""
        recursion_limit = 1
        direxp = DirectoryExplorer(start_dir=self.test_dir, show_hidden=False,
                                   recursion_limit=recursion_limit)
        results = direxp.explore()

        recr_depth = 0
        for dirs, _ in results:
            if dirs:
                if recr_depth > recursion_limit:
                    self.assertFalse(self.dir_pattern_a % recr_depth in dirs)
                    self.assertFalse(self.dir_pattern_b % recr_depth in dirs)
                else:
                    self.assertTrue(self.dir_pattern_a % recr_depth in dirs)
                    self.assertTrue(self.dir_pattern_b % recr_depth in dirs)
                recr_depth += 1

    def test_build_tree(self):
        """Test the build_tree method."""
        direxp = DirectoryExplorer(start_dir=self.test_dir, show_hidden=False)
        tree = direxp.build_tree()

        level = 0
        current_node = tree.get_root()
        while current_node.get_children():
            children = [ch.get_name() for ch in current_node.get_children()]
            self.assertTrue(self.dir_pattern_a % level in children)
            self.assertTrue(self.dir_pattern_b % level in children)

            if current_node.get_name() is self.dir_pattern_a % (level - 1):
                files = current_node.get_files()
                self.assertTrue(self.file_pattern_a % level in files)
                self.assertTrue(self.file_pattern_b % level in files)

            level += 1
            current_node = current_node.get_children()[0]


if __name__ == "__main__":
    unittest.main()
