import json
from pickletools import read_float8
import pyodbc
import pandas as pd

LocationTable = 'location'
UsersTable = 'users'

def InsertRowToDB(row):
    UserJson = GenUserJson(row)
    SQLInsert(UserJson, UsersTable)

#   Connect to SQL Server Database
def SqlConnect():
    conn = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=MARYAM-PC;'
        'Database=Mary01;'
        'UID=Mary;'
        'PWD=M@ryM@ryM@ry;'
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
    
    JsonUser['gender_id'] = GetGenderID(row['gender'])
    
    JsonUser['nationality_id'] = GetNationalityID(row['nat']) 
    
    GetLocationID = SQLInsert(GenLocationJson(row), LocationTable)
    JsonUser['location_id'] = GetLocationID
    
    return JsonUser

#   Generate Location Dictionary (Json) to be added to the Location table
def GenLocationJson(row):
    JsonLoc = {}
    JsonLoc['city'] = row['location']['city']
    JsonLoc['latitude'] = row['location']['coordinates']['latitude']
    JsonLoc['longitude'] = row['location']['coordinates']['longitude']
    return JsonLoc
    
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

#   Fetch gender_id from the gender table  
def GetGenderID(sex):
    cursor = SqlConnect()
    cursor.execute("SELECT * FROM gender") 
    Response = cursor.fetchall()
    for row in Response:
        if sex == row[1]:
            cursor.close()
            return row[0]
    print('Gender Not Found')
    cursor.close()
    exit(0)

#   Fetch nationality_id from the nationality table
def GetNationalityID(nat):
    cursor = SqlConnect()
    cursor.execute("SELECT * FROM nationality") 
    Response = cursor.fetchall()
    for row in Response:
        if nat == row[1]:
            cursor.close()
            return row[0]
    print('Nationality Not Found')
    cursor.close()
    exit(0)