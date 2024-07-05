# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 14:43:11 2022

@author: Tomek
"""
#%% Definitions
import os

def find_paths(rootPath= ".\\", is_path_ok= lambda path: True)->list:
    foundPaths= []
    for objName in os.listdir(rootPath):
        path= os.path.join( rootPath, objName)
        if is_path_ok(path): foundPaths.append(path)
        if os.path.isdir(path):
            foundPaths.extend( find_paths(path, is_path_ok) )
    return foundPaths

is_path_pdf_file= lambda path: path.endswith(".pdf") and os.path.isfile(path)

def decrypt_pdfs(rootPath= ".\\"):
    paths_to_pdfs= find_paths(rootPath, is_path_pdf_file)
    appPath= os.sys.argv[0]
    tempPath= appPath.removesuffix(".py")+".temp"; del appPath
    open(tempPath, "x")
    
    for path in paths_to_pdfs:
        print('Decrypting:\n\t"%s"'%path)
        
        os.system(f'qpdf --decrypt --replace-input "{path}" > "{tempPath}"')
        
        output= open(tempPath).read()
        if output:  os.sys.stderr.write(output)
        else:       print("Success!")
        print()
    os.remove(tempPath)
    
#%% App
rootPath= input("provide root path")
decrypt_pdfs(rootPath)
