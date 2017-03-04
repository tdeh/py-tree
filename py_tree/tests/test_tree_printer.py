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

"""This modules contains tests for the TreePrinter class.

Example:
    These tests can be run with the command::

        $ python -m py_tree.tests.test_tree_printer
"""

import os
import unittest
from mock import MagicMock
from ..tree_printer import TreePrinter


class TestTreePrinter(unittest.TestCase):
    """Unittest class containing tests for TreePrinter."""

    def setUp(self):
        n_children = 10

        # Initialize mock objects
        self._mock_tree = MagicMock()
        self._mock_children = []
        self._mock_root = MagicMock()

        for _ in range(n_children):
            mock_child = MagicMock()
            mock_child.get_children.return_value = []
            mock_child.get_files.return_value = []
            mock_child.get_symlinks.return_value = []
            mock_child.get_name.return_value = ""
            self._mock_children.append(mock_child)

        self._mock_root.get_children.return_value = self._mock_children
        self._mock_root.get_files.return_value = []
        self._mock_root.get_symlinks.return_value = []
        self._mock_root.get_name.return_value = ""

        self._mock_tree.get_root.return_value = self._mock_root

    def test_print_tree_visits_all(self):
        """Tests that print_tree will visit all nodes."""
        printer = TreePrinter(self._mock_tree)
        printer.print_tree()

        self._mock_tree.get_root.assert_called_once()
        self._mock_root.get_children.assert_called_once()
        self._mock_root.get_name.assert_called_once()

        for mock_node in self._mock_children:
            mock_node.get_children.assert_called_once()
            mock_node.get_name.assert_called_once()

    def test_print_tree_gets_all_files(self):
        """Tests that print_tree will get all files."""
        printer = TreePrinter(self._mock_tree)
        printer.print_tree()

        self._mock_tree.get_root.assert_called_once()
        self._mock_root.get_files.assert_called_once()

        for mock_node in self._mock_children:
            mock_node.get_files.assert_called_once()

    def test_print_tree_gets_all_links(self):
        """Tests that print_tree will get all symlinks."""
        printer = TreePrinter(self._mock_tree)
        printer.print_tree()

        self._mock_tree.get_root.assert_called_once()
        self._mock_root.get_symlinks.assert_called_once()

        for mock_node in self._mock_children:
            mock_node.get_symlinks.assert_called_once()

    def test_print_tree_writes_to_file(self):
        """Tests that print_tree will write to a file when specified."""
        filename = "testfile.txt"
        printer = TreePrinter(self._mock_tree, output_file=filename)
        printer.print_tree()

        self.assertTrue(filename in os.listdir("."))

        try:
            os.remove(filename)
        except OSError:
            pass


if __name__ == "__main__":
    unittest.main()
