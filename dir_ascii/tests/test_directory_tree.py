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

import unittest
from ..directory_tree import DirectoryTree, DirectoryNode


class TestDirectoryNode(unittest.TestCase):
    """Unittest class containing tests for DirectoryNode."""

    pass


class TestDirectoryTree(unittest.TestCase):
    """Unittest class containing tests for DirectoryTree."""

    def test_get_root(self):
        """Test the get_root() method."""
        root_name = "root"
        tree = DirectoryTree(root_name)
        self.assertEqual(tree.get_root(), tree._root)


if __name__ == "__main__":
    unittest.main()
