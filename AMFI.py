import openpyxl
# This part opens a new workbook and renames the sheet as "AMFI NAV".
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'AMFI NAV'
# This part asks for the file name. If the input length is less than 1, default name is taken as "NAVAll.txt". It will open the input file. 
name = input("Enter file: ")
if len(name) < 1 : name = "NAVAll.txt"
handle = open(name)
# This part reads the file line by line and splits words using semicolon. If the length of the words is less than 2 (meaning if there is some blank space in the beginning), then it will be ignored. And then 3 variables will picks up words based on the index and lastly append the same to the excel file.
for line in handle:
    words = line.split(';')
    if len(words) < 2: continue
    SchemeName = words[3]
    NAV = words[4]
    Date = words[5]
    sheet.append([SchemeName, NAV, Date])
# excel file is saved with the given name.
excel.save('AMFI NAV.xlsx')