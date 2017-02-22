# Dir-ASCII #

[![Build Status](https://travis-ci.org/tdeh/dir-ascii.svg?branch=master)](https://travis-ci.org/tdeh/dir-ascii)

## Overview ##

Creates an ASCII-based graphcial representation of directory hierarchies.

### Output for project hierarchy ###

```
.
|-- _config.yml
|-- apply_license.sh
|-- CONTRIBUTING.md
|-- LICENSE
|-- license_boilerplate
|-- README.md
|-- requirements.txt
`-- dir_ascii
    |-- __init__.py
    |-- __main__.py
    |-- directory_explorer.py
    |-- directory_tree.py
    |-- tree_printer.py
    `-- tests
        |-- __init__.py
        |-- __main__.py
        |-- test_directory_explorer.py
        |-- test_directory_tree.py
        `-- test_tree_printer.py
```

## Install ##

Run `pip install -r requirements.txt` to download all package dependencies.

## Usage ##

In the root project directory:

    python -m dir_ascii

To get argument details & descriptions:

    python -m dir_ascii -h

This should output something like:

```
usage: __main__.py [-h] [-s] [-d [DEPTH_LIMIT]] [-o [OUTPUT_FILE]]
                   [-w [INDENTATION_WIDTH]]
                   [start]

Creates text-based graphical of directory hierarchies.

positional arguments:
  start                 Path to start the search

optional arguments:
  -h, --help            show this help message and exit
  -s, --show_hidden     Show hidden files/directories e.g. .file, ..dir
  -d [DEPTH_LIMIT], --depth_limit [DEPTH_LIMIT]
                        Maximum directory depth to be explored
  -o [OUTPUT_FILE], --output_file [OUTPUT_FILE]
                        Write output to file name specified
  -w [INDENTATION_WIDTH], --indentation_width [INDENTATION_WIDTH]
                        The indentation width in number of spaces per
                        directory level. Min width is 2, default is 4.

```

## Running Unit Tests ##

### Option 1 ###

    py.test

### Option 2 ###

    python -m dir_ascii.tests

## Contributing ##

See [guidelines for contributions](CONTRIBUTING.md).
