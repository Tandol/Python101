import csv

def writecsv(datalist) :
    with open('data.csv', 'a', encoding = 'utf-8', newline = '') as file :
        fw = csv.writer(file) # fw = file writter
        fw.writerow(datalist) #[]

def readcsv() :
    with open('data.csv', encoding = 'utf-8', newline = '') as file :
        fr = csv.reader(file) # fw = file writter
        data =list(fr)
        return data


#readcsv()

data = ['ขนม', 'ชอคโกแลต', 20]
writecsv(data)