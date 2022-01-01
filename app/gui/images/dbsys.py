from typing import Type
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from popup import show_popup2, show_popup3, show_popup4, show_popup5
from user import thes_title, thes_abs, thes_type, thes_year
from scr import screen
from label import infos
from kivy.uix.image import Image
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
current_thes_type = ""
current_thes_year = ""

thesis = Table(
            "thesis", meta,
            Column('ID', Integer, primary_key = True),
            Column('TITLE', String(20)), 
            Column('ABSTRACT', String(50)), 
            Column('TYPE', String(20)),
            Column('YEAR', Integer)
        )

def create_table():
    thesis.create(db, checkfirst = True)
    print("Table is created.")
    show_popup2()

def delete_table():
    try:
        thesis.drop(db)
        bground = Image(source ='background.jpg')
        bground.pos = (-105, -100)
        screen.add_widget(bground)
        print("Table is deleted.")
        show_popup3()
        
    except:
        print("There is no table to delete.")
        show_popup4()

def title_callback(self):
    screen.remove_widget(thes_title)
    screen.add_widget(thes_abs)
    thes_abs.foreground_color = (1,0,0,1)
    thes_abs.bind(on_text_validate = abs_callback)

def abs_callback(self):
    screen.remove_widget(thes_abs)
    screen.add_widget(thes_type)
    thes_type.foreground_color = (1,0,0,1)
    thes_type.bind(on_text_validate = type_callback)

def type_callback(self):
    screen.remove_widget(thes_type)
    screen.add_widget(thes_year)
    thes_year.foreground_color = (1,0,0,1)
    thes_year.bind(on_text_validate = year_callback)

def year_callback(self):
    screen.remove_widget(thes_year)
    inserts()

def insert_to_table():
    global thes_counter
    screen.add_widget(thes_title)
    thes_title.foreground_color = (1,0,0,1)
    thes_title.bind(on_text_validate = title_callback)
    if len(thes_year.text) > 0 and thes_counter % 2 != 0:
        global current_thes_name
        global current_thes_abs
        global current_thes_type
        global current_thes_year
        current_thes_name = thes_title.text
        current_thes_abs = thes_abs.text
        current_thes_type = thes_type.text
        current_thes_year = thes_year.text
        thes_title.text = ""
        thes_abs.text = ""
        thes_type.text = ""
        thes_year.text = ""
        query = "INSERT INTO thesis VALUES ('{}','{}','{}','{}','{}')".format(thes_counter, current_thes_name, current_thes_abs, current_thes_type, current_thes_year)
        cnt.execute(query)
    thes_counter += 1
    print("Inserted.")

def read_table(self):
    try:
        user_table = pd.read_sql_table(table_name = "thesis", con = db)
        print(user_table)
        myInfo = str(user_table)
        infos(myInfo)
    except:
        show_popup5()

def inserts():
    global current_thes_name
    global current_thes_abs
    global current_thes_type
    global current_thes_year
    global thes_counter
    current_thes_name = thes_title.text
    current_thes_abs = thes_abs.text
    current_thes_type = thes_type.text
    current_thes_year = thes_year.text
    thes_title.text = ""
    thes_abs.text = ""
    thes_type.text = ""
    thes_year.text = ""
    query = "INSERT INTO thesis VALUES ('{}','{}','{}','{}','{}')".format(thes_counter, current_thes_name, current_thes_abs, current_thes_type, current_thes_year)
    cnt.execute(query)
    thes_counter += 1