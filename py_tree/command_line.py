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

"""This module handles the command line for py_tree.

Example:
    In order to run py_tree, use this command::

        $ python -m py_tree
"""

from argparse import ArgumentParser
from .directory_explorer import DirectoryExplorer
from .tree_printer import TreePrinter


def command_line_runner():
    """Parser args, builds a directory tree, and then prints it."""
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

    main(start_dir=args.start,
         show_hidden=args.show_hidden,
         depth_limit=args.depth_limit,
         indentation_width=args.indentation_width,
         output_file=args.output_file)


def main(start_dir=".", show_hidden=False, depth_limit=10, indentation_width=4,
         output_file=""):
    """Runs py_tree using the arguments provided.

    py_tree will traverse directories using the path provided (current dir if
    none is provided) and print a text-based tree of the result.

    Args:
        start_dir (str): Path to start the search.
        show_hidden (bool): Show hidden files/directories e.g. .file, ..dir.
        depth_limit (int): Maximum directory depth to be explored.
        indentation_width (int): The indentation width in number of spaces per
            directory level.
        output_file (str): Write output to file name specified.
    """
    # Build tree and print it
    explorer = DirectoryExplorer(start_dir=start_dir,
                                 show_hidden=show_hidden,
                                 recursion_limit=depth_limit)
    dir_tree = explorer.build_tree()
    printer = TreePrinter(tree=dir_tree,
                          indentation_width=indentation_width,
                          output_file=output_file)
    printer.print_tree()
