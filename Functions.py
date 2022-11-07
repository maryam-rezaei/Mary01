import pandas as pd
import Config as C

def GetNatXLSX():
# Exit if file does not exist
    try:
        with open(C.XLSX_PATH, "rb") as file:
            XLS_File = pd.read_excel(C.XLSX_PATH)
            Nat = ','.join(XLS_File['nationality'].tolist())
            return Nat.lower()
    # Raise error if the file does not exist
    except IOError:
        print("Excel file does not exist.")
        exit(0)

def GetNatCount():
    NatCount = {}
    XLS_File = pd.read_excel(C.XLSX_PATH)
    Nat = XLS_File['nationality'].tolist()
    Count = XLS_File['count'].tolist()

    for row in range (0, len(Nat)):
        if str(Count[row]).isnumeric():
            NatCount[Nat[row]] = Count[row]
        else:
            NatCount[Nat[row]] = '1'
    return NatCount
