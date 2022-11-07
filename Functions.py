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
