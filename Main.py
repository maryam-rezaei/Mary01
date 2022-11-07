import API
import SQL
import Functions as F

NatCount = F.GetNatCount()

for nat, count in NatCount.items():
    API_Data = API.GetData(nat, count)
    for row in API_Data["results"]:
        SQL.InsertRowToDB(row)