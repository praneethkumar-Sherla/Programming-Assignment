import csv
import requests # handle url stuff
import os
import MySQLdb


# Connect to MySQLDB 
mydb = MySQLdb.connect(localhost,user,passwd,database)
cursor = mydb.cursor()

 
for _ in range(100):           #downloading and uploading 100 csv files
    target_url=input('enter URL to download CSV file: ')
    data = requests.get(target_url)
    filename=input('enter file number (as save): ') #filename 
    with open(filename,'a+')as file:
        writer=csv.writer(file)
        writer.writerows(data)

    cursor.execute(filename) #storing csv file in db  
    print('File uploaded')

#closing db connections
    
mydb.commit()
cursor.close()
        
            
        
