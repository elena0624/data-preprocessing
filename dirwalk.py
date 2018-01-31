from os import walk

# 指定要列出所有檔案的目錄
mypath = "D:/txc/finaltest"

# 遞迴列出所有子目錄與檔案
i=0
filename = []          ## 空列表
for root, dirs, files in walk(mypath):
  #print("路徑：", root)
  #print("  目錄：", dirs)
#  filename[i]=files
  filename.append(files)   ## 使用 append() 添加元素
  #print("  檔案：", files)