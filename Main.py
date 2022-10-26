import API
import SQL

API_Data = API.GetData()

for row in API_Data["results"]:
    SQL.InsertRowToDB(row)