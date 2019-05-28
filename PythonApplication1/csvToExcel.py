import csv
import openpyxl

def konvertuj():
    try:
        wb = openpyxl.Workbook()
        ws = wb.active

        with open('C:\\Users\\r103co62\\Desktop\\Stanja 1205.csv') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                ws.append(row)

        wb.save('C:\\Users\\r103co62\\Desktop\\proba.xlsx')
        return 'uspesno'
    except:
        return 'ne valja'