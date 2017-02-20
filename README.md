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

## Running Unit Tests ##

### Option 1 ###

    py.test

### Option 2 ###

    python -m dir_ascii.tests

## Contributing ##

See [guidelines for contributions](CONTRIBUTING.md).
