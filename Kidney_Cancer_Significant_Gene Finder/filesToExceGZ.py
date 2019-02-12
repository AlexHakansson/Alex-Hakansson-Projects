import gzip
import os
import pandas as pd
import math
import numpy as np


import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def filesToTable (outFile, fileList, filler = "NA", varCol = 0, valCol =1):

    sep = "\t"
    dataDict = {}
    names = []
    count = 0
    for f in fileList:
        print(str(count) + " out of " + str(len(fileList)))
        count +=1
        with gzip.open(f,"rt") as reader:
            
            #data = [x.decode("utf8") for x in reader.readlines()]
            data = reader.readlines()
            varLoc = varCol
            valLoc = valCol
            if type(varCol) != int:
                header = data[0].strip().split("\t")
                for i in range(len(header)):
                    if header[i] == varCol:
                        varLoc = i
                if type(varLoc) != int:
                    continue
                    
            if type(valCol) != int:
                header = data[0].strip().split("\t")
                for i in range(len(header)):
                    if header[i] == valCol:
                        valLoc = i
                if type(valLoc) != int:
                    continue
                        
            name = os.path.basename(f).split(".tx")[0]      
            names.append(name)
           
          
            vars = [] #get variables
            values = {}
            
            for line in data:
                lineSplit = line.strip().split('\t')
                vars.append(lineSplit[varLoc])
                values[lineSplit[varLoc]] = lineSplit[valLoc]
                
            #add filler to any missing variables
            
            if len(names) > 1:
               
                for v in vars:
                    if v not in dataDict:
                        dataDict[v] = {} 
                        for k in names:
                            dataDict[v][k] = filler
            for v in vars:
                if not v in dataDict:
                    dataDict[v] = {}
                dataDict[v][name] = values[v]
                
            #keyList = dataDict[dataDict.keys()[0]].keys()
            for k in dataDict.keys():
                if k not in vars:
                    dataDict[k][name] = filler
    
    out = open(outFile, "w")
    keys = list(dataDict[k].keys())
    keys.sort()
    header = "\t".join(keys)
    header = "gene\t" +header
    out.write(header+"\n")
    
    for k in dataDict:
        strng = k 
        for n in keys:
            strng = strng + "\t" + str(dataDict[k][n])
        out.write(strng +"\n")
    out.close()
        
def fastFilesToTable(outFile,fileList):
        
        
        
    sep = "\t"
    dataDict = {}
    names = []
    count = 0
    length = -1
    out = open(outFile, "w")
    for f in fileList:
        print(str(count) + " out of " + str(len(fileList)))
        count +=1
        with gzip.open(f,"rt") as reader:
            

            name = os.path.basename(f).split(".tx")[0] 
            data = reader.readlines()
            
            first = False
            if length == -1:
                length = len(data)
                data = [x.strip().split("\t") for x in data]
                out.write("Patient\t")
                for i in data:
                    out.write(i[0] +"\t")
                out.write("\n")
                first = True
                
            
            if len(data) == length:
                out.write(name + "\t")
                if not first:
                    data = [x.strip().split("\t") for x in data]
                for i in data:
                    out.write(i[1] + "\t")
                out.write("\n")
                
    out.close()
    
def transAndRemoveLowVar (file, percentFiltered = 0, outfile = None):

    df = pd.read_csv(file, sep = "\t", header = 0, index_col = 0)
    df.loc["var"] = df.var(axis = 0, skipna = True, numeric_only = True)
    

    #print (df.loc["var"])
    if percentFiltered == 0: 
        threshold = 1
    else:
        varList = list(df.loc["var"])
        varList.sort()
        threshold = varList[math.ceil(len(varList)*percentFiltered)]

    print(threshold)
    print("filtering")
   
    df = df.loc[:, df.loc["var"] > threshold]
    df = df.loc[:, df.loc["var"] != np.nan]
    #for col in df.columns:
     #   if df.loc["var",col] <= threshold or np.isnan(df.loc["var",col]):
      #      df.drop(col, axis = 1)
            
    print("Transposing")
    df = df.transpose()
    
    if outfile != None:
        df.to_csv(outfile, sep = "\t")
        
    return df
    
    
def removeLowExpressed (data, minMean =1, outfile = None):
    if type(data) == str:
        df = pd.read_csv(file, sep = "\t", header = 0, index_col = 0)
    else:
        df = data
    
    df.loc[:,"mean"] = df.mean(axis = 1, skipna = True, numeric_only = True)
    print (df.loc[:,"mean"])
    df = df.loc [df.loc[:,"mean"] > minMean,:]
    
    if outfile != None:
        df.to_csv(outfile, sep = "\t")
        
    return df
    
    
def plotHist (df, row, outfile, bins = 100):
    
    plt.hist(df.loc[:,row], bins, facecolor='blue')
    plt.savefig(outfile)
    