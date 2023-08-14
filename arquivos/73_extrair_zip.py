from zipfile import ZipFile
import os

filename = "../dados_externos/2022.zip"
os.mkdir("../dados_externos/2022")

with ZipFile(filename, 'r') as filezip:
    filezip.printdir()  # lista os arquivos do zip
    filezip.extractall('../dados_externos/2022')

