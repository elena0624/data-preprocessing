# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:02:25 2018

@author: Eugene&Yvonne&joukey
"""
import numpy as np
import re
import pandas as pd
from io import StringIO
from os import walk, listdir
import xlrd
from pandas.core.frame import DataFrame
import time

mypath = "D:\\TXCexp\\inter4state\\"


lotnamelist = listdir('D:\\TXCexp\\inter4state')

def getfeature(mypath):
    path=[]
    path2=[]
    for root, dirs, files in walk(mypath):
        if len(files)>0:
            path.append([root,files])
            
    for i in range(len(path)):
        for j in range(len(path[i][1])):
            path2.append(path[i][0]+'\\'+path[i][1][j])
    
    rightdflist = list()
    BLKdf = list()
    RETdf = list()
    PKGdf = list()
    LASdf = list()
    FRQdf = list()
    FNLdf = list()
    BNDdf = list()
    LOGdf = list()
    QNTdf = list()
    LOTdf = list()
    CSVdf = list()
    XLSdf = list()
    falsedf = list()
    falsefile = list()
    Filelist = list()
    errorlist = list()
    tStart = time.time()
    for i in range(len(path2)):#len(path2)
        try:
            if "BLK"in path2[i]:
                Filelist.append(path2[i])
                f = open(path2[i], 'r')
                raw = f.read()
                f.close()
                data = re.split('"<|\n"<|>"\n',raw)
                BLKdf.append(pd.read_csv(StringIO(data[4])))
            elif "RET" in path2[i]:
                Filelist.append(path2[i])
                f = open(path2[i], 'r')
                raw = f.read()
                f.close()
                data = re.split('"<|\n"<|>"\n',raw)
                RETdf.append(pd.read_csv(StringIO(data[4])))
            elif "PKG" in path2[i]:
                Filelist.append(path2[i])
                f = open(path2[i], 'r')
                raw = f.read()
                f.close()
                data = re.split('"<|\n"<|>"\n',raw)
                PKGdf.append(pd.read_csv(StringIO(data[4])))
            elif "LAS" in path2[i]:
                Filelist.append(path2[i])
                f = open(path2[i], 'r')
                raw = f.read()
                f.close()
                data = re.split('"<|\n"<|>"\n',raw)
                LASdf.append(pd.read_csv(StringIO(data[4])))
            elif "FNL" in path2[i]:
                Filelist.append(path2[i])
                f = open(path2[i], 'r')
                raw = f.read()
                f.close()
                data = re.split('"<|\n"<|>"\n',raw)
                FNLdf.append(pd.read_csv(StringIO(data[4])))
            elif "BND" in path2[i]:
                Filelist.append(path2[i])
                f = open(path2[i], 'r')
                raw = f.read()
                f.close()
                data = re.split('"<|\n"<|>"\n',raw)
                tempdf = pd.read_csv(StringIO(data[4]))
                tempdf = tempdf.apply(lambda x: x.str.strip() if isinstance(x, str) else x).replace('Null', np.nan)
                tempdf.iloc[:,1:10] =(tempdf.iloc[:,1:10]).convert_objects(convert_numeric=True)
                BNDdf.append(tempdf)
            elif "FRQ" in path2[i]:
                Filelist.append(path2[i])
                f = open(path2[i], 'r')
                raw = f.read()
                f.close()
                data = re.split('\n',raw)
                FRQdf.append(pd.DataFrame(line.strip().split(',') for line in data))
            elif "LOG" in path2[i]:
                Filelist.append(path2[i])
                LOGdf.append(pd.read_csv(path2[i]))
            elif "QNT" in path2[i]:
                Filelist.append(path2[i])
                QNTdf.append(pd.read_csv(path2[i]))
            elif "LOT" in path2[i]:
                Filelist.append(path2[i])
                LOTdf.append(pd.read_csv(path2[i]))
            elif "XLS" in path2[i]:
                Filelist.append(path2[i])
                book = xlrd.open_workbook(path2[i])
                sh = book.sheet_by_index(0)
                nrows=sh.nrows
                data=[]
                title=sh.row_values(11)
                for i in range(18,nrows):
                    row_data=sh.row_values(i)
                    data.append(row_data)
                FINAL=DataFrame(data)
                FINAL.columns = title
                FINAL = FINAL.apply(lambda x: x.str.strip() if isinstance(x, str) else x).replace('', np.nan)
                XLSdf.append(FINAL)
            elif "CSV" in path2[i]:
                Filelist.append(path2[i])
                f = open(path2[i], 'r')
                raw = f.read()
                f.close()
                data = re.split('<|\n<|>\n',raw)
                CSVdf.append(pd.read_csv(StringIO(data[8])))
            else:
                falsefile.append(path2[i])
                falsedf.append(path2[i])
        except:
            errorlist.append(path2[i])
        print(i)
    
    usefullist = list()
    rightdflist = [BLKdf, PKGdf, LASdf, FNLdf, BNDdf, QNTdf, LOGdf, CSVdf, XLSdf] #exclude: FRQdf, LOTdf, RETdf
    for i in range(len(rightdflist)):
        if len(rightdflist[i])>1:
            usefullist.append(pd.concat(rightdflist[i]))
    #        usefullist.append(pd.concat((rightdflist[i]), axis=0, ignore_index=True))
        elif len(rightdflist[i]) == 1:
            usefullist.append(rightdflist[i][0])
        elif len(rightdflist[i]) == 0:
            rightdflist[i] = []
    deslist = list()
    deserrlist = list()
    for df in usefullist:
        try:
            deslist.append(df.describe())
        except:
            deserrlist.append(df)
    
    # 將每個mean&std取出
    #stats = list()
    stats={}
    stats['mean']=pd.DataFrame()
    stats['std'] = pd.DataFrame()
    for i in range(len(deslist)):
        temp = deslist[i].loc['mean']
        tempstd = deslist[i].loc['std']
        stats['mean'] = pd.concat([stats['mean'], temp])
        stats['std'] = pd.concat([stats['std'], tempstd])
    
    stats['mean'] = stats['mean'].transpose()
    stats['std'] = stats['std'].transpose()
    tEnd = time.time()
    print (tEnd - tStart)
    return stats
i=0
all_stats={}
all_stats['mean'] = pd.DataFrame()
all_stats['std'] = pd.DataFrame()
tempAns = list()
for path in lotnamelist[0:41]:#lotnamelist
    newpath = mypath+path
    tempAns.append(getfeature(newpath)) 
#    all_stats['mean'] = pd.concat([all_stats['mean'],tempAns['mean']])
#    all_stats['std'] = all_stats['std'].append(tempAns['std'])