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

import os
import shutil
import unittest
from ..directory_explorer import DirectoryExplorer


class TestDirectoryExplorer(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.abspath("./test_dir/") + "/"
        os.mkdir(self.test_dir)

        self.hidden_files = [".hidfile.txt", "..hidfile.txt"]
        self.hidden_dirs = [".hiddir", "..hiddir"]

        for f in self.hidden_files:
            self._make_file(self.test_dir + f)

        for d in self.hidden_dirs:
            os.mkdir(self.test_dir + d)

        self.dir_pattern_a = "dira%i"
        self.dir_pattern_b = "dirb%i"
        self.file_pattern_a = "filea%i.txt"
        self.file_pattern_b = "fileb%i.txt"

        path = self.test_dir
        for i in range(3):
            self._make_file(path + (self.file_pattern_a % i))
            self._make_file(path + (self.file_pattern_b % i))
            os.mkdir(path + (self.dir_pattern_a % i))
            os.mkdir(path + (self.dir_pattern_b % i))
            path = os.path.join(path, self.dir_pattern_a % i) + "/"

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def _make_file(self, filename):
        open(filename, 'a').close()

    def test_explore_hides_hidden_files(self):
        direxp = DirectoryExplorer(start_dir=self.test_dir, show_hidden=False)
        results = direxp.explore()
        _, files = results[0]

        for f in self.hidden_files:
            self.assertFalse(f in files)

    def test_explore_hides_hidden_dirs(self):
        direxp = DirectoryExplorer(start_dir=self.test_dir, show_hidden=False)
        results = direxp.explore()
        dirs, _ = results[0]

        for d in self.hidden_dirs:
            self.assertFalse(d in dirs)

    def test_explore_shows_hidden_files(self):
        direxp = DirectoryExplorer(start_dir=self.test_dir, show_hidden=True)
        results = direxp.explore()
        _, files = results[0]

        for f in self.hidden_files:
            self.assertTrue(f in files)

    def test_explore_shows_hidden_dirs(self):
        direxp = DirectoryExplorer(start_dir=self.test_dir, show_hidden=True)
        results = direxp.explore()
        dirs, _ = results[0]

        for d in self.hidden_dirs:
            self.assertTrue(d in dirs)

    def test_explore_finds_all_files(self):
        direxp = DirectoryExplorer(start_dir=self.test_dir, show_hidden=False)
        results = direxp.explore()

        recursion_level = 0
        for _, files in results:
            if files:
                self.assertTrue(self.file_pattern_a % recursion_level in files)
                self.assertTrue(self.file_pattern_b % recursion_level in files)
                recursion_level += 1

    def test_explore_finds_all_dirs(self):
        direxp = DirectoryExplorer(start_dir=self.test_dir, show_hidden=False)
        results = direxp.explore()

        recursion_level = 0
        for dirs, _ in results:
            if dirs:
                self.assertTrue(self.dir_pattern_a % recursion_level in dirs)
                self.assertTrue(self.dir_pattern_b % recursion_level in dirs)
                recursion_level += 1


if __name__ == "__main__":
    unittest.main()
