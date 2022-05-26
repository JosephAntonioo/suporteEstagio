####Variaveis de suporte em ordem de necessidade nem tudo sao flores
caminho = "Downloads/grade-exportacao.pdf"

####Variaveis de suporte em ordem de necessidade nem tudo sao flores

# Arquivo Python de Suporte para ser usada na Main.py e caso haja necessidade ser replicado em outros lugares no futuro :)
# PSEUDO CÓDIGO(?code?)
#
# 
#1ºExtracting Text From a PDF -> https://realpython.com/creating-modifying-pdf/#extracting-text-from-a-pdf
#   Primeiro temos que extrair os dados para o que precisamos
from time import sleep
from PyPDF2 import PdfFileReader as PFR
##CRIAR FUNCTION DAQUI ATÉ**************************************
#Import para pegar o path do arquivo
from pathlib import Path
pdf_path = (Path.home() / caminho)
#print(pdf_path)
pdf = PFR(str(pdf_path))
##OPÇÕES 
print("pdf.getNumPages()---->" + str(pdf.getNumPages()))
print("pdf.documentInfo---->" + str(pdf.documentInfo))
print("pdf.documentInfo.title---->" + str(pdf.documentInfo.title))
while(0 < 1):
    print('pausa para banheiro agua café é isso trabalha em alto nivel precisa esticar um pouco')
    sleep(10)
    
#Extracting Text From a Page

##AQUI POR ENQUANTO*********************************************

#   Segundo temos que tratar esses dados ainda nesse primeiro passo, o que garante que pegou certo? que é 
#   o tipo de arquivo 
#
#2ºCreating a PDF File From Scratch -> https://realpython.com/creating-modifying-pdf/#creating-a-pdf-file-from-scratch
#   Em seguida precisamos efetivamente criar o PDF que vamos gerar ou sejá lá como for pois existem caminhos
#   de tratamento diferentes para cada dado
#   Para ai sim fazer a divisão de para quem vai ser enviado o dado e como será tratado 

#