import PyPDF2
import os


if(os.path.isdir("temp") == False):                 #Check if there is a folder called temp
    os.mkdir("temp")                                #If it doesn't exist (False), then os.mkdir("temp") creates it.
                                                    #Purpose: to have a directory(FILE) where text files will be saved if you don't provide one explicitly.
    
txtpath = ""
pdfpath = ""



pdfpath = input("Enter the name of your pdf file - please use backslash when typing in directory path: ")   #Provide the path for your pdf here
txtpath = input("Enter the name of your txt file - please use backslash when typing in directory path: ")   #Provide the path for the output text file  

BASEDIR = os.path.realpath("temp") # This is the sample base directory where all your text files will be stored if you do not give a specific path
print(BASEDIR)


if(len(txtpath) == 0):                                                                                              
    txtpath = os.path.join(BASEDIR,os.path.basename(os.path.normpath(pdfpath)).replace(".pdf", "")+".txt")          
    
"""If you didn't give a path for the text file (len(txtpath) == 0):
Build one automatically:
os.path.basename(os.path.normpath(pdfpath)) → takes the name of the PDF file (without directories).
.replace(".pdf", "") → removes the .pdf extension.
Append .txt → becomes the name of the text file.
Puts it in the temp directory.
"""

pdfobj = open(pdfpath, 'rb')                        #Open the PDF file in rb mode (read binary)
pdfread = PyPDF2.PdfFileReader(pdfobj)              #Create a reader object for the PDF.
x = pdfread.numPages                                #numPages → total number of pages in the PDF.


for i in range(x):                                  
    pageObj = pdfread.getPage(i)                    
    with open(txtpath, 'a+') as f:                  
        f.write((pageObj.extractText()))
    print(pageObj.extractText()) #This just provides the overview of what is being added to your output, you can remove it if want
"""
Iterate through each page (for i in range(x)).
getPage(i) → get page i.
pageObj.extractText() → extract text from page.
Write text to .txt file (mod a+ = append to file, if already exists).
print(...) → print text to console (for viewing only).
"""                       

pdfobj.close()        #Close the PDF file opened at the beginning (good practice to free up resources).
