from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from user import thes_title, thes_abs
from scr import screen
import pandas as pd

POSTGRES_DB = "database"
POSTGRES_USER = "postgres"
POSTGRES_PW = "12345"
POSTGRES_HOST = "127.0.0.1"

# Connect to the database 
DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(POSTGRES_USER, POSTGRES_PW, POSTGRES_HOST, POSTGRES_DB)
db = create_engine(DATABASE_URI, echo = True)
cnt = db.connect()
meta = MetaData()
thes_counter = 1000
current_thes_name = ""
current_thes_abs = ""


thesis = Table(
            "thesis", meta,
            Column('THES_ID', Integer, primary_key = True),
            Column('THES_TITLE', String(20)), 
            Column('THES_ABS', String(50)), 
            Column('THES_TYPE', String(20)),
            Column('THES_YEAR', Integer)
        )

def create_table(): 
    thesis.create(db, checkfirst = True)

def delete_table():
    thesis.drop(db)

def title_callback(self):
    screen.remove_widget(thes_title)
    screen.add_widget(thes_abs)
    thes_abs.foreground_color = (1,0,0,1)
    thes_abs.bind(on_text_validate = abs_callback)

def abs_callback(self):
    screen.remove_widget(thes_abs)
    inserts()

def insert_to_table():
    global thes_counter
    screen.add_widget(thes_title)
    thes_title.foreground_color = (1,0,0,1)
    thes_title.bind(on_text_validate = title_callback)
    if len(thes_abs.text) > 0 and thes_counter % 2 != 0:
        global current_thes_name
        global current_thes_abs
        current_thes_name = thes_title.text
        current_thes_abs = thes_abs.text
        thes_title.text = ""
        thes_abs.text = ""
        query = "INSERT INTO thesis VALUES ('{}','{}','{}')".format(thes_counter, current_thes_name, current_thes_abs)
        cnt.execute(query)
    thes_counter += 1

def read_table(self):
    user_table = pd.read_sql_table(table_name = "thesis", con = db)
    print(user_table)

def inserts():
    global current_thes_name
    global current_thes_abs
    global thes_counter
    current_thes_name = thes_title.text
    current_thes_abs = thes_abs.text
    thes_title.text = ""
    thes_abs.text = ""
    query = "INSERT INTO thesis VALUES ('{}','{}','{}')".format(thes_counter, current_thes_name, current_thes_abs)
    cnt.execute(query)
    thes_counter += 1