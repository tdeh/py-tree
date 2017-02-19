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

"""This module contains the TreePrinter class.

The TreePrinter is used to create a graphical representation of a DirectoryTree
object and write it to stdout.
"""

import sys


class TreePrinter(object):
    """Prints a graphical representation of a DirectoryTree obejct.

    This class exposes a print_tree() method which will print a graphical
    representation of the tree.

    Args:
        tree (DirectoryTree): The tree to be printed.
        indentation_width (int): Width in terms of characters for the
            indentation levels
        output_file (str): File to redirect output to. If None, write to stdout.

    Attributes:
        _tree (DirectoryTree): The tree to be printed.
            originate.
        _indentation_width (int): The character width of each indentation level.
        _indent_str (str): String that represents a single indentation level.
        _entry_prefix (str): The prefix printed before an entry under a
            directory.
        _end_prefix (str): The prefix printed before the last entry under a
            directory.
    """

    # Static constants for formatting characters
    LEVEL_CHAR = '|'
    ENTRY_CHAR = '-'
    END_CHAR = '`'

    def __init__(self, tree, indentation_width=4, output_file=None):
        if indentation_width < 2:
            raise Exception("Indentation width must be 2 or greater!")

        self._tree = tree
        self._indentation_width = indentation_width

        # Indentation string
        self._indent_str = TreePrinter.LEVEL_CHAR.ljust(self._indentation_width,
                                                        ' ')

        # Prefix for an entry
        self._entry_prefix = TreePrinter.LEVEL_CHAR.ljust(
            self._indentation_width-1,
            TreePrinter.ENTRY_CHAR)
        self._entry_prefix += ' '

        # Prefix for the end entry
        self._end_prefix = TreePrinter.END_CHAR.ljust(self._indentation_width-1,
                                                      TreePrinter.ENTRY_CHAR)
        self._end_prefix += ' '

        # If an output file is specified, redirect stdout to file
        if output_file:
            sys.stdout = open(output_file, 'w')

    def _print_recursive(self, node, indent_str):
        """Recursive method called on all nodes to print children and files.

        This method will recursively call itself on all children of the
        specified node.

        Args:
            node (DirectoryNode): The current node being visited.
            indent_str (str): The string to be printed as indentation.
        """
        # Get this node's files and children
        files = node.get_files()
        children = node.get_children()

        # Initialize length variables
        n_files = len(files)
        n_children = len(children)

        # Print this node's files
        for i in range(n_files):
            entry = indent_str + self._entry_prefix + files[i]

            # If this is the last file and there are no children, use the end
            # prefix instead of the normal prefix
            if n_children <= 0 and i + 1 == n_files:
                entry = indent_str + self._end_prefix + files[i]

            print(entry)  # pylint: disable=superfluous-parens

        # Recursively call on all children
        child_indent_str = indent_str + self._indent_str
        for i in range(n_children):
            child = children[i]
            prefix = self._entry_prefix

            # If this is the last child, use the end prefix else use the normal
            # entry prefix
            if i + 1 == n_children:
                child_indent_str = indent_str + " " * self._indentation_width
                prefix = self._end_prefix

            print(indent_str + prefix + child.get_name())  # pylint: disable=superfluous-parens
            self._print_recursive(child, child_indent_str)

    def print_tree(self):
        """Prints the tree provided to the constructor."""
        root = self._tree.get_root()
        print(root.get_name())  # pylint: disable=superfluous-parens
        self._print_recursive(root, "")
