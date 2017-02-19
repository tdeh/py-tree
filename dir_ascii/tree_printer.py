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

        # If an output file is specified, redirect stdout
        if output_file:
            sys.stdout = open(output_file, 'wb')

    def _print_recursive(self, node, level):
        # Print this node and it's files
        if level <= 0:
            print(node.get_name()) # pylint: disable=superfluous-parens
        else:
            dirname = self._indent_str * (level - 1) + self._entry_prefix + \
                node.get_name()
            print(dirname) # pylint: disable=superfluous-parens

        for filename in node.files():
            file_entry = self._indent_str * level + self._entry_prefix + \
                filename
            print(file_entry) # pylint: disable=superfluous-parens

        # Recursively call on all children
        for child in node.children():
            self._print_recursive(child, level + 1)

    def print_tree(self):
        self._print_recursive(self._tree.get_root(), 0)
