import time
import random
from sqlalchemy import create_engine

POSTGRES_DB = "database"
POSTGRES_USER = "postgres"
POSTGRES_PW = "12345"
POSTGRES_HOST = "127.0.0.1"

# Connect to the database 
DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(POSTGRES_USER, POSTGRES_PW, POSTGRES_HOST, POSTGRES_DB)
db = create_engine(DATABASE_URI)

def create_table(): 
  	# Create a table
    query = "CREATE TABLE IF NOT EXISTS numbers (number BIGINT,timestamp BIGINT);"
    db.execute(query)
    
def add_new_row(n):
    # Insert a new number into the 'numbers' table.
    db.execute("INSERT INTO numbers (number,timestamp) "+
        "VALUES ("+
        str(n) + "," + 
        str(int(round(time.time() * 1000))) + ");")

def get_last_row():
    # Retrieve the last number inserted inside the 'numbers'
    query = "SELECT number FROM numbers WHERE timestamp >= (SELECT max(timestamp) FROM numbers) LIMIT 1" 

    result_set = db.execute(query)  
    for (r) in result_set:  
        return r[0]

if __name__ == "__main__":
    print('Application started')
    
    while True:
        time.sleep(5)
        create_table()	
        add_new_row(random.randint(1,100000))
        print('The last value insterted is: {}'.format(get_last_row()))