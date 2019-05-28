#using pandas
def loadExcel():
    import pandas as pd

    file = 'C:\\Users\\r103co62\\Desktop\\Template.xlsx'

    #xl = pd.ExcelFile(file)

    #print(xl.sheet_names)

    #df1 = xl.parse('Sheet1')
    df1 = pd.read_excel(file)
    print(type(df1))
    columns = list(df1)
    columnTypes = []
    for item in df1.dtypes:
        columnTypes.append(str(item))
    print(columns)
    print(columnTypes)
    #print(df1.dtypes) #column types
    #print(list(df1)) #column names

    #df1.to_csv('C:\\Users\\r103co62\\Desktop\\proba.csv',';')

  
#using pyexcel
def loadExcelPy():
    import pyexcel
    file = 'C:\\Users\\r103co62\\Desktop\\Template.xlsx'
    # Get an array from the data
    my_array = pyexcel.get_array(file_name=file)
    print(my_array)


#ucitaj u dictionary
def loadExcelInDict():
    import pyexcel
    from pyexcel._compact import OrderedDict
    file = 'C:\\Users\\r103co62\\Desktop\\Template.xlsx'
    # Get your data in an ordered dictionary of lists
    my_dict = pyexcel.get_dict(file_name=file, name_columns_by_row=0)
    # Get your data in a dictionary of 2D arrays
    book_dict = pyexcel.get_book_dict(file_name=file)
    # Retrieve the records of the file
    records = pyexcel.get_records(file_name=file)
    #print(my_dict)
    #print(book_dict)
    #print(records)
    #sheet1 = book_dict.get('Sheet1')
    #print(sheet1[0])
    #zaglavlja = sheet1[0]
    #if 'ID' in zaglavlja:
    #    print('Ima ID')
    #else:
    #    print('nema ID')
    #sheet1.pop(0)
    #for x in sheet1:
    #    if(x[2] > 24):
    #        print(x[1] + ' je stariji od 24')
    #    else:
    #        print(x[1] + ' nije stariji od 24')
    #import _csv as csv
    #outfile = open('C:\\Users\\r103co62\\Desktop\\proba.csv', 'w')
    #writer = csv.writer(outfile, delimiter=';', lineterminator='\n' ,quotechar='"')
    #writer.writerows(sheet1)
    #outfile.close()

#funkcija koja pretvara excel u csv za new image
def toCsv(excel):
    import pyexcel
    import datetime
    from pyexcel._compact import OrderedDict
    book_dict = pyexcel.get_book_dict(file_name=excel)
    sheet1 = book_dict.get('Sheet1')
    zaglavlja = sheet1[0]
    lista = []
    datumi = []
    pozicija = 0
    for z in zaglavlja:
        if('iznos' in z.lower()):
            lista.append(pozicija)
        if 'datum' in z.lower():
            datumi.append(pozicija)
        pozicija += 1
    #print(lista)
    if(len(lista) > 0):
        for x in sheet1:
            for i in lista:
                x[i] = str(x[i]).replace(',', '.')
    if len(datumi) > 0:
        for x in sheet1:
            for i in datumi:
                if type(x[i]) == type(datetime.datetime.now()):
                    x[i] = x[i].strftime('%d.%m.%Y')
                    #x[i] = 'asasa'
                #x[i] = type(x[i])
    #print(sheet1)
    import _csv as csv
    outfile = open('C:\\Users\\r103co62\\Desktop\\test\\Podaci za klijente 30.01.2019-21.02.2019.csv', 'w')
    writer = csv.writer(outfile, delimiter=';', lineterminator='\n' ,quotechar='"')
    writer.writerows(sheet1)
    outfile.close()
