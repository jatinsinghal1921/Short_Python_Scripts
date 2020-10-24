import win32com.client # need to install pywin32
import os

excel = win32com.client.Dispatch("Excel.Application")
workbook = excel.ActiveWorkbook

wb_folder = workbook.Path
wb_name = workbook.Name
wb_path = os.path.join(wb_folder, wb_name)

print("Extracting data from {}".format(wb_path))
