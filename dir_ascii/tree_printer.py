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

import sys


class TreePrinter(object):

    # Static constants for some formatting characters
    LEVEL_CHAR = '|'
    ENTRY_CHAR = '-'
    END_CHAR = '`'

    def __init__(self, tree, indentation_width=4, output_file=None):
        if indentation_width < 2:
            raise Exception("Indentation width must be 2 or greater!")

        self._tree = tree
        self._indentation_width = indentation_width

        # Initialize indentation and entry prefix strings
        self._indent_str = TreePrinter.LEVEL_CHAR.ljust(self._indentation_width,
                                                        ' ')
        self._entry_prefix = TreePrinter.LEVEL_CHAR.ljust(
                                                    self._indentation_width-1,
                                                    TreePrinter.ENTRY_CHAR)
        self._entry_prefix += ' '
        self._end_prefix = TreePrinter.END_CHAR.ljust(self._indentation_width-1,
                                                      TreePrinter.ENTRY_CHAR)
        self._end_prefix += ' '

        # If an output file is specified, redirect stdout
        if output_file:
            sys.stdout = open(output_file, 'wb')

    def _print_recursive(self, node, indent_str):
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

            print(entry) # pylint: disable=superfluous-parens

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

            print(indent_str + prefix + child.get_name())
            self._print_recursive(child, child_indent_str)

    def print_tree(self):
        root = self._tree.get_root()
        print(root.get_name())  # pylint: disable=superfluous-parens
        self._print_recursive(root, "")
