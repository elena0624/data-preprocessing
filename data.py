# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:02:25 2018

@author: Eugene&Yvonne
"""
import re
import pandas as pd
from io import StringIO
from os import walk
import xlrd
from pandas.core.frame import DataFrame
import time
tStart = time.time()

mypath = "D:\\txc\\inter4state"
path=[]
path2=[]
for root, dirs, files in walk(mypath):
    if len(files)>0:
        path.append([root,files])
for i in range(len(path)):
    for j in range(len(path[i][1])):
        path2.append(path[i][0]+'\\'+path[i][1][j])

kind1 = []
kind2 = []
kind3 = []
kind4 = []
kind5 = []
kind6 = []
File1 = []
File2 = []
File3 = []
File4 = []
File5 = []
errorlist = []#test

#第一次跑BA,BB 3642
#BC 18420
#for i in range(len(path2)):
#改成dictionary裡面存
for i in range(0,3643):
    try:
        if ("BLK"in path2[i]) or ("BND" in path2[i]) or ("FNL" in path2[i]) or ("LAS" in path2[i]) or ("PKG" in path2[i]) or ("RET" in path2[i]):
            File1.append(path2[i])
            f = open(path2[i], 'r')
            raw = f.read()
            f.close()
            data = re.split('"<|\n"<|>"\n',raw)
            kind1.append(pd.read_csv(StringIO(data[4])))
        elif "FRQ" in path2[i]:
            File2.append(path2[i])
            f = open(path2[i], 'r')
            raw = f.read()
            f.close()
            data = re.split('\n',raw)
            kind2.append(pd.DataFrame(line.strip().split(',') for line in data))
        elif ("LOG" in path2[i]) or ("LOT" in path2[i]) or ("QNT" in path2[i]):
            File3.append(path2[i])
            kind3.append(pd.read_csv(path2[i]))
        elif "XLS" in path2[i]:
            File4.append(path2[i])
            book = xlrd.open_workbook(path2[i])
            sh = book.sheet_by_index(0)
            nrows=sh.nrows
            data=[]
            title=sh.row_values(11)
            for i in range(18,nrows):
                row_data=sh.row_values(i)
                data.append(row_data)
            FINAL=DataFrame(data)
            FINAL.columns = [title]
            kind4.append(FINAL)
            book.release_resources()
            del book
        elif "CSV" in path2[i]:
            File5.append(path2[i])
            f = open(path2[i], 'r')
            raw = f.read()
            f.close()
            data = re.split('<|\n<|>\n',raw)
            kind5.append(pd.read_csv(StringIO(data[8])))
        else:
            kind6.append(path2[i])
    except:
        errorlist.append(path2[i])
    print(i)

tEnd = time.time()
print (tEnd - tStart)