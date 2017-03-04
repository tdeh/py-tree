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

"""This module is the entry point for py_tree.

Example:
    In order to run py_tree, use this command::

        $ python -m py_tree
"""

from argparse import ArgumentParser
from .directory_explorer import DirectoryExplorer
from .tree_printer import TreePrinter


def main():
    """Parsers args, builds a directory tree, and then prints it."""
    # Setup argument parsing
    parser = ArgumentParser(
        description="""
        Creates text-based graphical representations of directory hierarchies.
        """)
    parser.add_argument("start", type=str, nargs="?", default=".",
                        help="Path to start the search")
    parser.add_argument("-s", "--show_hidden", action="store_true",
                        help="Show hidden files/directories e.g. .file, ..dir")
    parser.add_argument("-d", "--depth_limit", nargs="?", default=10, type=int,
                        help="Maximum directory depth to be explored")
    parser.add_argument("-o", "--output_file", nargs="?", default="", type=str,
                        help="Write output to file name specified")
    parser.add_argument("-w", "--indentation_width", nargs="?", default=4,
                        type=int,
                        help="""
                        The indentation width in number of spaces per directory
                        level. Min width is 2, default is 4.
                        """)
    args = parser.parse_args()

    # Build tree and print it
    explorer = DirectoryExplorer(start_dir=args.start,
                                 show_hidden=args.show_hidden,
                                 recursion_limit=args.depth_limit)
    dir_tree = explorer.build_tree()
    printer = TreePrinter(tree=dir_tree,
                          indentation_width=args.indentation_width,
                          output_file=args.output_file)
    printer.print_tree()


if __name__ == "__main__":
    main()
