import pygsheets
import pandas as pd
import datetime
import os
from app.util import email

SPREADHSHEET="py-sheet-demo"
EXPORT_DIR="exports"

queries=[]


class PyGoogleSheet:
    def __init__(self,service_file_path='/Users/erikrood/desktop/QS_Model/creds.json'):
        self.gc = pygsheets.authorize(service_file=service_file_path)

    def get_gc(self):
        return gc   

    def open_spreadsheet(self,sheet_name="Sheet1"):
        return self.gc.open(sheet_name)     

    def open_spreadsheet_by_key(self,sheet_key):
        return self.gc.open_by_key(sheet_key)  

    def open_spreadsheet_by_url(self,sheet_url):
        self.gc.open_by_url(sheet_url)    

    def get_spreadsheet_id(self):
        return self.gc.id    

    def delete_spreadsheet(self): 
        self.gc.delete()  

    def get_last_updated(self): 
        return self.gc.updated 

    def get_spreadsheet_url(self): 
        return self.gc.url      

    """sumary_line
    
    Keyword arguments:
    argument --
    Return: return_description
    """
    
    def share_spreadsheet(self,emails=[],share_message="Here is the spreadsheet we talked about!",role="reader",type="user"):

        emails = map(str, emails)
        for email in emails:

            self.sh.share(email.strip(), emailMessage=share_message, role=role,type=type)        


class PyReport:

    def __init__(self, py_google_sheet):
        self.py_reporter_sheet = py_google_sheet
        self.sheet = None
        self.df = None

    def open_sheet(self,sheet_name):
        if self.py_reporter_sheet is None:
            raise ValueError("PyGoogleSheet instance cannot be null")

        self.sheet = self.py_reporter_sheet.open_spreadsheet(sheet_name)
        return self.sheet

    def select_worksheet(self, sheet, title="Sheet1"):
        if sheet is None:
            raise ValueError("Sheet cannot cannot be null")
        return sheet.worksheet_by_title(title)    

    def load_sheet_into_pd(self, work_sheet):
        self.df = pd.DataFrame(work_sheet.get_all_records())
        print(self.df)
        return self

    def export_data_csv(self,filename):
        cur_date = create_today_date_str()
        self.df.to_csv(f"{EXPORT_DIR}/csv/{cur_date}-{filename}")

    def export_data_excel(self,filename):
        cur_date = create_today_date_str()
        self.df.to_excel(f"{EXPORT_DIR}/excel/{cur_date}-{filename}")  


    def clean_user_data(self):
        if self.df is None:
            return
        self.df.drop_duplicates(keep='first',inplace=True) #drop duplicates    
        self.df.dropna()    

    def generate_report(self, report_name="hr-department-report"):
        #self.clean_user_data()
        #report code goes here
        pass    

def create_today_date_str():
    x = datetime.datetime.now()
    date = x.strftime("%Y-%m-%d")
    return date

def create_export_folders():
    create_folder(f"{EXPORT_DIR}/excel")
    create_folder(f"{EXPORT_DIR}/csv")

def create_folder(folder_name):
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print("created folder : ", folder_name)
  
  

def main():
    print("main func")
    #---create export folders 
    create_export_folders()

    #---
    py_reporter = PyReport(PyGoogleSheet("py-sheet-reporter-5ff955c9c02c.json"))
    #open spreadhsheet
    sheet = py_reporter.open_sheet(SPREADHSHEET)
    print("print sheet")
    print(sheet)
    print("select worksheet")
    wrk = py_reporter.select_worksheet(sheet,"Sheet1")
    print(wrk)
    #-----
    print("print wrk df")
    py_reporter.load_sheet_into_pd(wrk)


    #--send email 
    #build message
    msg = email.build_simple_message()
    print("msg", msg)



if __name__ == "__main__":
    main()