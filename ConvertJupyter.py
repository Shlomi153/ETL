#Created by Shlomi Kiko
#Goal: This program converts Jupyter notebooks format ipynb to .py format so that it can be run via Jenkins and executes the files.
#LinkedIn: https://www.linkedin.com/in/shlomikiko/

import os
import subprocess
import fnmatch
import shutil
import glob
import json

devEnv = """
#########################################################################
#Dev environment:
#########################################################################
"""
print(devEnv)

devSourceDir = r'C:\SourcePath'
devSourceDirFiles = os.listdir(devSourceDir)

devTargetDir = r'C:\TargetPath'
filesToConvert = []

#Filter out unecessary files and append relevant files to list - Dev
for file in devSourceDirFiles:
    if not fnmatch.fnmatch(file, '*checkpoint*') and not fnmatch.fnmatch(file, 'DevLogs') and not fnmatch.fnmatch(file, '*.py'):
        devSourceFilePath = devSourceDir + '\\' + file
        filesToConvert.append(devSourceFilePath)

#Convert to py format so that we can run it for all relevant files - Dev
for file in filesToConvert:
    code = json.load(open(file))

    with open(f'{file}.py', 'w+') as pyFileDev:
        for cell in code['cells']:
            if cell['cell_type'] == 'code':
                for line in cell['source']:
                    pyFileDev.write(line)
                pyFileDev.write("\n")
            elif cell['cell_type'] == 'markdown':
                pyFileDev.write("\n")
                for line in cell['source']:
                    pyFileDev.write('#' + line)
                pyFileDev.write("\n")

print('Completed converting all the Dev Notebooks into .Py format.\n')

#Move .Py files to another location in order to avoid confusion - Dev
devSourcePyList = glob.glob(devSourceDir + '\\' + '*.py')
devTargetPyFilesPath = []

for sourceFilePath in devSourcePyList:
    fileName = os.path.basename(sourceFilePath)
    devTargetPyFilesPath.append(devTargetDir + '\\' + fileName)
    shutil.move(sourceFilePath, devTargetDir + '\\' + fileName)

print('Files moved successfully for Dev environment!\n')

prodEnv = """
###########################################################################
#Prod environment:
###########################################################################
"""
print(prodEnv)

prodSourceDir = r'C:\SourcePath'
prodSourceDirFiles = os.listdir(devSourceDir)

prodTargetDir = r'C:\TargetPath'
filesToConvert = []

#Filter out unecessary files and append relevant files to list - Dev
for file in prodSourceDirFiles:
    if not fnmatch.fnmatch(file, '*checkpoint*') and not fnmatch.fnmatch(file, 'devLogs') and not fnmatch.fnmatch(file, '*.py'):
        prodSourceFilePath = prodSourceDir + '\\' + file
        filesToConvert.append(prodSourceFilePath)

#Convert to py format so that we can run it for all relevant files - Prod
for file in filesToConvert:
    code = json.load(open(file))

    with open(f'{file}.py', 'w+') as pyFileProd:
        for cell in code['cells']:
            if cell['cell_type'] == 'code':
                for line in cell['source']:
                    pyFileProd.write(line)
                pyFileProd.write('\n')
            elif cell['cell_type'] == 'markdown':
                pyFileProd.write('\n')
                for line in cell['source']:
                    pyFileProd.write('#' + line)
                pyFileProd.write('\n')

print('Completed converting all the Prod Notebooks into .Py format.\n')

#Move .Py files to another location in order to avoid confusion - Prod
prodSourcePyList = glob.glob(prodSourceDir + '\\' + '*.py')
prodTargetPyFilesPath = []

for sourceFilePath in prodSourcePyList:
    fileName = os.path.basename(sourceFilePath)
    prodTargetPyFilesPath.append(prodTargetDir + '\\' + fileName)

    shutil.move(sourceFilePath, prodTargetDir + '\\' + fileName)

print('Files moved successfully for Prod environment!\n')

#Final confirmation
finalConfirmation = """
###########################################################################
#Files converted and moved successfully for all environments!
###########################################################################
"""
print(finalConfirmation)

##########################################################################
#Execute .Py files
##########################################################################

for file in devTargetPyFilesPath:
   subprocess.call(["python", file])

print('All Dev files executed successfully!\n')

for file in prodTargetPyFilesPath:
   subprocess.call(["python", file])

print('All Prod files executed successfully!\n')
