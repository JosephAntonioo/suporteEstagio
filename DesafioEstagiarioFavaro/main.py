from time import sleep
from PyPDF2 import PdfFileReader as PFR
from pathlib import Path

from numpy import empty
from sqlalchemy import false
caminho = "grade-exportacao.pdf"
#1ºExtracting Text From a PDF -> https://realpython.com/creating-modifying-pdf/#extracting-text-from-a-pdf
#   Primeiro temos que extrair os dados para o que precisamos
# pdf_path = (Path.home() / caminho)
#print(pdf_path)
# pdf = PFR(str(pdf_path))
##OPÇÕES 
# print("pdf.getNumPages()---->" + str(pdf.getNumPages()))
# print("pdf.documentInfo---->" + str(pdf.documentInfo))
# print("pdf.documentInfo.title---->" + str(pdf.documentInfo.title))
# while(0 < 1):
#     print('pausa para banheiro agua café é isso trabalha em alto nivel precisa esticar um pouco')
#     sleep(10)
    
def pegaPDF(caminho):
    pdf_path = ( caminho)
    pdf = PFR(str(pdf_path))
    if(pdf):
        print(false)
        return false
    print([pdf, true])
    return [pdf, true]

def main(caminho):
    pegaPDF(caminho)
    
app = main(caminho)
print(caminho)