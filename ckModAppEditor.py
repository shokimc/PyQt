
def saveText(fileName, text):
    f = open(fileName, 'w')
    f.write(text)
    f.close()
    return True
    
def readText(fileName):
    f = open(fileName, 'r')
    text=f.read()
    f.close()
    return text
