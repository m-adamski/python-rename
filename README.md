# Python Rename Tool

Simple Python script written for personal use for mass renaming of files. The script can generate a list of files from a
given location and save it to a CSV file. The main functionality is to rename files according to the indicated CSV file
containing a column with the current file name and the new file name.

## Installation

The module uses additional packages that must be installed with the package installer for Python. To do this, run the
command:

```commandline
pip install -r requirements.txt
```

## Running the module

```commandline
python main.py summary ./source
python main.py summary ./source --csv summary.csv
python main.py rename ./source --csv summary.csv --columns filename rename
```

## Virtual environment

The venv module provides support for creating "virtual environments" with your own independent set of Python packages.
In order to prepare a virtual environment, we must first create it and then connect to it:

```commandline
python -m venv ./venv && source ./venv/Scripts/activate
```

Instead of installing packages globally, we can only install them in a created virtual environment.

In order to run the module with automatic connection to the virtual environment, the bin/run-venv.sh file has been
prepared. Just run the command in the console:

```commandline
bin/run-venv.sh summary ./source --csv summary.csv
```

## License

GNU General Public License