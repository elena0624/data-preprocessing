# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 22:52:45 2018

@author: peipeiju
"""
import os, sys
from os import walk
import shutil as sh


def simple_revise(dirs):
    for i in range(len(dirs)):
        dirs[i]=dirs[i].replace(" ","")# 處理有些空白部分
        dirs[i]=dirs[i][0:9]#取前9個字元
        dirs[i]=dirs[i].upper()#把前兩碼都變成大寫
        #8c打成88c的就先忽略
        #要現在rename嗎?
    return dirs

# Final test資料系列
mypath = "D:/txc"
# 遞迴列出所有子目錄與檔案
filename = []          ## 空列表
for root, dirs, files in walk(mypath):
#    filename.append(files)   ## 使用 append() 添加元素
#    filenametest = os.listdir(root)
#    print(filenametest)
    os.chdir(root)
    for name in files:
        try:
            os.rename(name, name.replace(" ", "").upper())
        except FileExistsError:
            os.rename(name, name.replace(" ", "_emptyerr").upper())

#final=[]
#for i in range(len(filename)):
#    final=final+simple_revise(filename[i])


#intersection=list(set(bp) & set(final))

for dirname in intersection: #create newdir for same lot name
    os.mkdir("D:/txc/newdata/{}".format(dirname))

#for root, dirs, files in walk(mypath):
#    os.chdir(root)
#    for name in files:
#        sh.copy(name, 'D:/txc/newdata/{}'.format(name[0:9]))
