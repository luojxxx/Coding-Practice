import os
folderpath = '/Users/cloudlife/Desktop/'
def openFile(fileName):
    return open( fileName, 'r').read().split()

def openFile(fileName):
    data = []
    for row in open(fileName, 'r'):
        data.append(row.strip().split(' '))
    return data

def checkAgainstTest(customFn, inputFile, outputFile):
    dataIn = openFile(inputFile)
    dataOut = openFile(outputFile)
    dataIn.pop(0)
    results = [ customFn(float(linein)) == float(lineout) for linein, lineout in zip(dataIn, dataOut) ]
    return results, dataIn, dataOut