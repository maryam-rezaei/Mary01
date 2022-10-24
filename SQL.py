import pyodbc
import pandas as pd

conn = None

def SqlConnect():
    global conn
    conn = pyodbc.connect('Driver={SQL SERVER};'
                    'Server=MARYAM-PC;'
                    'Database=mary01;'
                    'Trusted_Connection=yes;')
    cursor = conn.cursor()
    print(conn)
