
def writedata():
    with open('data.txt' , 'w', encoding = 'utf-8') as file :
        file.write('Hello world')

def adddata(text):
    with open('adddata.txt','a', encoding = 'utf-8') as file :
        file.write('\n' + text)
        


adddata('samorn')
