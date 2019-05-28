##thislist = ["apple", "banana", "cherry"]
##for x in thislist:
##  print(x) 

##x = 2j
##y = 3j
##print(x+y)
#file = open("C:\\Users\\r103co62\\Desktop\\Pravno lice.txt", "r")
#text = file.read()
#text = text.lower()
##print(text)
##niz = text.split()
#import re
#niz = re.split('[. ,\n()-+*/"\'\n\r]', text)
#words_dict = {}
##for x in niz:
##    print(x)    
##print(niz)
#for word in niz:
#    words_dict[word] = words_dict.get(word,0)+1

#for key in sorted(words_dict):
#  print("{} : {}".format(key,words_dict[key])) 


import WorkWithExcel as excel
#excel.loadExcel()
#excel.loadExcelPy()
#excel.loadExcelInDict()
#excel.toCsv('C:\\Users\\r103co62\\Desktop\\test\\Podaci za klijente 30.01.2019-21.02.2019.xlsx')


import pythonAndMongoDb as mongo
from bson.objectid import ObjectId
#mongo.GetListOfDatabases()
#mongo.GetListOfCollectionsInDatabase("MyDb")
#mongo.GetRecordsFromCollection("MyDb", "Users")
#user = {"Ime": "Miodrag", "Prezime": "Jankovic", "Godine": 1, "JMBG": "2404018710011", "Adresa": {}}
#mongo.InsertOne("MyDb", "Users", user)
#query = {"_id": ObjectId("5c347af1ac7b820aacd06d03")}
#newValues = {"$set" : {"Adresa": {"Mesto": "Beograd", "Ulica": "", "Broj": 0, "ZIP": "1100"}}}
#mongo.UpdateOne("MyDb", "Users", query, newValues)

import sendFileOnFtpServer as ftp
#ftp.uploadToFtp('C:\\Users\\r103co62\\Desktop\\165140319_1.otp' , '165140319_1.otp')
#import csvToExcel
#csvToExcel.konvertuj()

import regex
#string = 'a7ikolaJd_5454'
#print(regex.provera(string)) #and regex.pocetak(string))

import pythonAndTxt as pytxt
#pytxt.readLinByLine('C:\\Users\\r103co62\\Desktop\\opomene\\RET_3_567861_AA17111HBS04_RSD_MAIN_20190301_1')
pytxt.deleteEmptyLines('C:\\Users\\r103co62\\Desktop\\test dva potpisa\\minus.csv')
pytxt.obrisiNeispravnePostanskeBrojeve('C:\\Users\\r103co62\\Desktop\\test dva potpisa\\novi.csv')