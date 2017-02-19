# Dir-ASCII #

[![Build Status](https://travis-ci.org/tdeh/dir-ascii.svg?branch=master)](https://travis-ci.org/tdeh/dir-ascii)

## Overview ##

Creates an ASCII-based graphcial representation of directory hierarchies.

### Output for project hierarchy ###

```
.
|-- requirements.txt
|-- CONTRIBUTING.md
|-- LICENSE
|-- _config.yml
|-- apply_license.sh
|-- license_boilerplate
|-- README.md
`-- dir_ascii
    |-- directory_tree.pyc
    |-- tree_printer.py
    |-- __main__.py
    |-- __init__.py
    |-- directory_explorer.pyc
    |-- directory_explorer.py
    |-- directory_tree.py
    |-- __init__.pyc
    |-- tree_printer.pyc
    `-- tests
        |-- test_directory_tree.py
        |-- __main__.py
        |-- __init__.py
        |-- test_tree_printer.py
        `-- test_directory_explorer.py
```

## Install ##

Run `pip install -r requirements.txt` to download all package dependencies.

## Usage ##

In the root project directory:

    python -m dir_ascii

## Running Unit Tests ##

### Option 1 ###

    py.test

### Option 2 ###

    python -m dir_ascii.tests

## Contributing ##

See [guidelines for contributions](CONTRIBUTING.md).
