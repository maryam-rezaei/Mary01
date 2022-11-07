import json
from pickletools import read_float8
import pyodbc
import pandas as pd
import Config as C

UserTable = 'user_table'

def InsertRowToDB(row):
    UserJson = GenUserJson(row)
    SQLInsert(UserJson, UserTable)

#   Connect to SQL Server Database
def SqlConnect():
    conn = pyodbc.connect(
        'Driver={SQL Server};'
        f'Server={C.SERVER};'
        f'Database={C.DATABASE};'
        f'UID={C.USERNAME};'
        f'PWD={C.PASSWORD};'
        'Trusted_Connection=no;'
    )
    cursor = conn.cursor()
    return cursor

#   Generate User Dictionary (Json) to be added to the User table
def GenUserJson(row):
    JsonUser = {}
    
    JsonUser['first_name'] = row['name']['first']
    JsonUser['last_name'] = row['name']['last']
    JsonUser['date_of_birth'] = (row['dob']['date'])[0:10]
    JsonUser['gender'] = row['gender']
    JsonUser['nationality'] = row['nat'] 
    JsonUser['country'] = row['location']['country']
    JsonUser['city'] = row['location']['city']
    JsonUser['latitude'] = row['location']['coordinates']['latitude']
    JsonUser['longitude'] = row['location']['coordinates']['longitude']
    
    return JsonUser
    
#   To Insert into tables in SQL Server    
def SQLInsert(Data, SQLTable):
    
    cursor = SqlConnect()
    columns = ', '.join(str(x).replace('/', '_') for x in Data.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in Data.values())
    SQLQuery = """INSERT INTO %s ( %s ) OUTPUT Inserted.ID VALUES ( %s );""" % (SQLTable, columns, values)
    cursor.execute(SQLQuery)
    
    ID = cursor.fetchone()[0]
    cursor.commit()
    cursor.close()
    return ID
