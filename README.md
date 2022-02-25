# py_google_sheet_reporter

# python in use [Python 3]
/usr/local/bin/python3

# upgrade pip if already installed
python3 -m pip install --user --upgrade pip

# install virtualenv
python3 -m pip install --user virtualenv

## create virtual environment
python3 -m venv env

## activate virtual environment
source env/bin/activate

## deactivate virtual environment
deactivate

# Update requirements file
## use this to rewrite requirement file whenever we update package
pip freeze > requirements.txt