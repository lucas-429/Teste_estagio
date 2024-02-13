import gspread as gsp
from google.oauth2.service_account import Credentials
from logic import Logic


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
]

# input the path of the json file that contains the credentials of the Google cloud platform
json_file = input('Digite o caminho do arquivo json de suas credenciais: ')

creds = Credentials.from_service_account_file(json_file, scopes=scopes)

client = gsp.authorize(creds)

sheet_id = '1pdfLU9hvd7E_nX7yYfgLSMVU2qi-6RAdMRf6nbHp97I'

sheet = client.open_by_key(sheet_id)  # Open the spreadsheet

worksheet = sheet.get_worksheet(0)  # Get the first sheet of the spreadsheet

column_situation = 7
column_naf = 8  # naf column, naf is the grade that the student needs to get in the final exam

range_of_update = 'G4:H27'
range_of_grades = 'D4:F27'
range_of_absent = 'C4:C27'
range_cells_grade = worksheet.get(range_of_grades)
range_cells_absent = worksheet.get(range_of_absent)
result = []

for x in range(24):
    logic = Logic(range_cells_grade[x][0], range_cells_grade[x][1], range_cells_grade[x][2], range_cells_absent[x][0])
    result.append(logic.approval())

worksheet.update(result, range_of_update)

""" too slow
for x in range(4, 28):
    logic = Logic(worksheet.cell(x, 4).value,
                  worksheet.cell(x, 5).value,
                  worksheet.cell(x, 6).value,
                  worksheet.cell(x, 3).value)

    worksheet.update_cell(x, column_situation, logic.approval()[0])  # update the situation column

    sleep(2)  # sleep for 2 seconds because the Google sheets api has a limit of requests per minutes

    worksheet.update_cell(x, column_naf, logic.approval()[1])  # update the naf column

    sleep(2)  # sleep for 2 seconds because the Google sheets api has a limit of requests per minutes
"""
