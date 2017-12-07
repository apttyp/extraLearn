import os
import sqlite3

db_file = 'ohaha.db'
emm = not os.path.exists(db_file)
conn = sqlite3.connect(db_file)
if emm:
    print("not exist!Create!")
else:
    print("exsit!")
conn.close()