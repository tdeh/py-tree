# Py-Tree #

[![Build Status](https://travis-ci.org/tdeh/py-tree.svg?branch=master)](https://travis-ci.org/tdeh/py-tree)

A command line tool for generating text-based representations of file hierarchies.

```
$ py-tree
.
|-- _config.yml
|-- apply_license.sh
|-- CONTRIBUTING.md
|-- LICENSE
|-- license_boilerplate
|-- MANIFEST.in
|-- README.md
|-- setup.py
`-- py_tree
    |-- __init__.py
    |-- __main__.py
    |-- command_line.py
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

### Users ###

**py-tree** is registered on the [Python Package Index](https://pypi.python.org/pypi/py-tree) and can be installed via `pip`:
```bash
pip install py-tree
```

### Developers ###

Clone repository and run this `pip` command from the root project directory:
```bash
pip install -e .
```

## Usage ##

### Linux Terminal ###

Setuptools should create a standalone script for running **Py-Tree** and add it to your *PATH*. To run this script:
```bash
$ py-tree
```

To get argument details & descriptions:
```bash
$ py-tree -h
```

This should output something like:

```
usage: py-tree [-h] [-s] [-d [DEPTH_LIMIT]] [-o [OUTPUT_FILE]]
               [-w [INDENTATION_WIDTH]]
               [start]

Creates text-based graphical representations of directory hierarchies.

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

### Python Console ###

To run from an interactive Python session:
```python
import py_tree
py_tree.main()
```

To get argument details & descriptions:
```python
help(py_tree.main)
```

## Running Unit Tests ##

For testing you need to install aditional testing dependencies from the `requirements.txt` file in the `tests` directory. Run this `pip` command from the root project directory:
```bash
pip install -r tests/requirements.txt
```
and then run the tests with:
```bash
pytest -v tests
```

## Linting ##

Install **pylint**:

```bash
pip install pylint
```

Run on code directory:

```bash
pylint py_tree
```

## Contributing ##

See [guidelines for contributions](CONTRIBUTING.md).

## License ##

Apache License, Version 2.0
