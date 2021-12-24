# Requirements for project
## PostgreSQL 13.5 [Link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
## Phyton 3.8.10 [Link](https://www.python.org/ftp/python/3.8.10/python-3.8.10-embed-amd64.zip)
!!Please check environment column for accesing pyhton commands.


# Setup 
## On app folder 
python -m venv virtual-env
For Windows:
source "venv/scripts/activate"
pip install -r requirements.txt
For Linux/MacOS
source venv/bin/activate
pip install -r requirements.txt

# Run
python -u app.py
# Run UI
python -u kivy.py