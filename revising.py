# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:01:32 2018

@author: peipeiju
"""

import os, sys

def revising(path):
    dirs = os.listdir(path)    
    for i in range(len(dirs)):
        dirs[i]=dirs[i].replace(" ","")# 處理有些空白部分
        dirs[i]=dirs[i][0:9]#取前9個字元
        dirs[i]=dirs[i].upper()#把前兩碼都變成大寫
        #8c打成88c的就先忽略
        #要現在rename嗎?
    return dirs


# 打开文件
# BP資料系列
a2f=revising("D:/txc/A2F/BP_Data")
b1f=revising("D:/txc/B1F/BP_Data")
c2f=revising("D:/txc/C2F/BP_Data")
c3f=revising("D:/txc/C3F/BP_Data")

# Final test資料系列

    
    