import ftplib
from ftplib import FTP

def uploadToFtp(filePath, fileName):
    ftp = FTP('10.34.3.21')
    #ftp = FTP('10.172.6.7')
    try:
        ftp.login('hipo', 'h165o39')
        ftp.cwd('RPG')
        #print(ftp.pwd())
        ftp.set_pasv(True)
        file = open(filePath, 'rb')
        ftp.storbinary('STOR ' + fileName, file) 
        print('uspesno ste poslali fajl')
    except Exception as e:
        print(str(e))
    finally:
        ftp.quit()
        #file.close()