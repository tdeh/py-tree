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

"""This modules contains tests for the DirectoryTree and DirectoryNode class.

Example:
    These tests can be run with the command::

        $ python -m dir_ascii.tests.test_directory_tree
"""

import unittest
from ..directory_tree import DirectoryTree, DirectoryNode


class TestDirectoryNode(unittest.TestCase):
    """Unittest class containing tests for DirectoryNode."""

    def setUp(self):
        self.node_name = "node"
        self.node = DirectoryNode(self.node_name)

    def test_get_name(self):
        """Test the get_name() method."""
        self.assertEqual(self.node_name, self.node.get_name())

    def test_add_child_get_children(self):
        """Test add_child and get_children methods."""
        n_children = 50
        name_template = "child%i"

        for i in range(n_children):
            self.node.add_child(name_template % i)

        child_dirs = self.node.get_children()
        for i in range(n_children):
            self.assertEqual(child_dirs[i].get_name(), name_template % i)

    def test_add_file_get_files(self):
        """Test add_file and get_files methods."""
        n_files = 50
        name_template = "file%i"

        for i in range(n_files):
            self.node.add_file(name_template % i)

        files = self.node.get_files()
        for i in range(n_files):
            self.assertEqual(files[i], name_template % i)

    def test_add_files_get_files(self):
        """Test add_files and get_files methods."""
        n_files = 50
        file_list = []
        name_template = "file%i"

        for i in range(n_files):
            file_list.append(name_template % i)

        self.node.add_files(file_list)

        files = self.node.get_files()
        for i in range(n_files):
            self.assertEqual(files[i], name_template % i)

    def test_children_generator(self):
        """Test the get_children generator method."""
        n_children = 50
        name_template = "child%i"

        for i in range(n_children):
            self.node.add_child(name_template % i)

        i = 0
        for child in self.node.children():
            self.assertEqual(child.get_name(), name_template % i)
            i += 1

    def test_files_generator(self):
        """Test the get_files generator method."""
        n_files = 50
        name_template = "file%i"

        for i in range(n_files):
            self.node.add_file(name_template % i)

        i = 0
        for filename in self.node.get_files():
            self.assertEqual(filename, name_template % i)
            i += 1

    def test_get_last_child(self):
        """Test the get_last_child method."""
        # Test on empty list
        self.assertIsNone(self.node.get_last_child())

        # Test on populated list
        n_children = 50
        name_template = "child%i"

        for i in range(n_children):
            self.node.add_child(name_template % i)

        self.assertEqual(self.node.get_last_child().get_name(),
                         name_template % (n_children - 1))


class TestDirectoryTree(unittest.TestCase):
    """Unittest class containing tests for DirectoryTree."""

    def test_get_root(self):
        """Test the get_root() method."""
        root_name = "root"
        tree = DirectoryTree(root_name)
        self.assertEqual(root_name, tree.get_root().get_name())


if __name__ == "__main__":
    unittest.main()
