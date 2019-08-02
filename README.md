# comic2pdf
A script to convert comic files (cbr, cbz) to pdf, in python3.

## Getting Started

### Installing

Install the package using [setuptools](https://github.com/pypa/setuptools).

```
$ python setup.py install
```

### Running

The `comic2pdf` command should be globally available, pass as arguments the path(s) to the cbr / cbz files and optionally specify an output folder. The output files will be named the same as the input files but with a .pdf extension.

```
usage: comic2pdf [-h] [-o OUTDIR] [--version] path [path ...]

Converts .cbr and .cbz files to .pdf

positional arguments:
  path                  paths to process

optional arguments:
  -h, --help            show this help message and exit
  -o OUTDIR, --outdir OUTDIR
                        directory to place generated files
  --version             show program's version number and exit
```

e.g. to process all files in a folder (will ignore any file extensions except .cbr, .cbz, .rar or .zip).

```
$ comic2pdf *
```

### Prerequisites

Requires Python 3.6+.

Production dependencies are listed in `setup.py`. Development dependencies are listed in `requirements.txt`.

### No install

You can use the package without installing it, simply install dependencies and run the `comic2pdf.py` script. E.g.

```
$ pip install -r requirements.txt
$ python comic2pdf.py -o /dest/folder file.cbr
```

## Development

### Installing 

Development is aided by a Makefile which uses a virtual environment. To setup the virtual environment and install dependencies:

```
$ make init
```

### Running

To test changes to your script, you can install a development version which links to your source code:

```
$ python setup.py develop
```

And this can be uninstalled with 

```
$ python setup.py develop --uninstall
```

You may also run the script directly, but note that the dependencies are installed into the virtual environment. To enter the virtual environment:

```
# Windows
$ source .venv/Scripts/activate
# Mac
$ source .venv/bin/activate
```

Then run the script directly.

```
(.venv) $ python comic2pdf.py -h
```

### Linting & formatting

This project makes use of the [Black](https://github.com/psf/black) python code formatter which automatically reformats code. To run Black and lint the code, use:

```
$ make lint
```

### Publishing

1. Update `setup.py` with the new version number (e.g. 1.1.1)
2. Create a new GitHub release (e.g. `git tag -a v1.1.1 -m "Version v1.1.1" && git push --tags`)
3. Push to PyPI
```
$ make deploy
```
## Authors and Acknowledgments

* **phdesign**
* **MComas1** (https://github.com/MComas1/comics2pdf)
* **bransorem** (https://github.com/bransorem/comic2pdf)
