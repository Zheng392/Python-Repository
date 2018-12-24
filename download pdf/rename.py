from PyPDF2 import PdfFileReader
import os


for i in range(4):
    for j in range(6):
        path = 'vol%d/issue%d'%(51+i,1+j)
        for file in os.listdir(path):
            pdfFileReader = PdfFileReader(os.path.join(path,file))
            documentInfo = pdfFileReader.getDocumentInfo()
            name = documentInfo['/Title']
            name=name.replace('/',' ')
            name = name.replace(':', ' ')
            name = name.replace('\\', ' ')
            name = name.replace('*', ' ')
            name = name.replace('?', ' ')
            name = name.replace('"', ' ')
            name = name.replace('<', ' ')
            name = name.replace('>', ' ')
            name = name.replace('|', ' ')
            print(os.path.join(path, file))
            os.rename(os.path.join(path, file), os.path.join(path,name+".pdf"))