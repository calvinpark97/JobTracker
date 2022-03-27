from openpyxl import Workbook, load_workbook

wb = Workbook()

ws = wb.active
ws.title = "Jobs"

for x in 15:
    ws.append
wb.save('time.xlsx')





