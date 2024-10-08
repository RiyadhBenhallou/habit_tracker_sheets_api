import gspread
from datetime import datetime 
import os

gc = gspread.service_account(filename='./credentials.json')
sheet_id = os.environ['SHEET_ID']

sh = gc.open_by_key(sheet_id)

def main():
    worksheet = sh.sheet1
    user_input = input('What did you do today?: ')
    today = datetime.today()
    data_to_append = [str(today.strftime('%Y/%m/%d')), *user_input.split(', ')]
    # Append the entire list to the worksheet in one go
    worksheet.append_row(data_to_append)


if __name__ == '__main__':
    main()
