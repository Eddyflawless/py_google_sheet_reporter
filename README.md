# py_google_sheet_reporter

Pre-requisites to run this project
Python 3.x installed on the system
pandas and mysql library installed (can be installed easily using pip)

SMTP mode setup on sender's mailing server

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

#note
dont forget to add the account serice account email to the spreadhseet