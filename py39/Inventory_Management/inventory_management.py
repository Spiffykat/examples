import os
import csv
import time

#uility vars
myBooks = '1_Owned_Books.csv'


def read_content():
    with open(myBooks, 'r') as file:
        r = csv.reader(myBooks)
        for row in r:
            print(file.read())

def write_content():
    with open(myBooks, 'a') as file:
        w = csv.DictWriter(file, fieldnames=["ID",
                            "Title",
                            "Author",
                            "Publisher",
                            "Serial",
                            "Status",
                            "Notes",
                            "Date"],
                    lineterminator='\n')

        w.writerow({'Title':title, 
                    'Author':author, 
                    'Publisher':publisher, 
                    'Serial':serial, 
                    'Status':status, 
                    'Notes':notes, 
                    'Date':time.strftime("%m/%d/%Y")})

#Days of learning here, global must be removed...
def entry():
    global title, author, publisher, serial, status, notes
    title = input("Title: ")
    author = input("Author: ")
    publisher = input("Publisher: ")
    serial = input("Serial: ")
    status = input("Status: ")
    notes = input("Notes: ")


#check if file exsist
if os.path.isfile(myBooks):
    print ('File is there')
    file = 0
else:
    print ('no file')
    file = 1
    
#Build ENV
if file == 1:
    print ('Creating File')
    with open(myBooks, 'w', encoding='utf-8') as file:
        w = csv.DictWriter(file, fieldnames=["ID",
                            "Title",
                            "Author",
                            "Publisher",
                            "Serial",
                            "Status",
                            "Notes",
                            "Date"],
                    lineterminator='\n')
        w.writeheader()
else:
    print ('Opening File and reading content...')
    read_content()

entry()
write_content()
read_content()