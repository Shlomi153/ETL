#Author: Shlomi Kiko
#Topic: This program takes JupyterNotebook files and converts from ipynb format to py format
#Linkedin: https://www.linkedin.com/in/shlomikiko/

import os
import subprocess
import shutil
import fnmatch
import glob
from pathlib import Path

jupyterNotebooksDir = r'C:\Users\shlom\JupyterLab'
filesInDir = os.listdir(jupyterNotebooksDir)
targetLocation = r'D:\Python Projects\Python ETL\ConvertedPy'

filesToConvert = []
fileNames = []

#Filter out irrelevant files
for file in filesInDir:
    if not fnmatch.fnmatch(file, '*py') and not fnmatch.fnmatch(file, '*checkpoints')  and not fnmatch.fnmatch(file, 'spark-warehouse'):
        filesToConvert.append(jupyterNotebooksDir + '\\' + file)
        fileNames.append(Path(file).stem)

#Convert the files to .py format
for file in filesToConvert:
    print(file)
    subprocess.call(f'jupyter nbconvert --to python {file}')

print('\nCompleted converting ipynb files to py format!\n')

#Move files to other directory to avoid confusion
sourceFilesPy = jupyterNotebooksDir + '\\' 
targetFilesPy = targetLocation + '\\'

#First delete any existing .py files there
filesInTarget = os.listdir(targetLocation)

for file in fileNames:
    if file + '.py' in filesInTarget:
        os.remove(targetFilesPy + file + '.py')

for file in glob.glob(sourceFilesPy + '*.py'):
    shutil.move(file, targetFilesPy)

print('Files moved successfully!\n')