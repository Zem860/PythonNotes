import os
import shutil

#可以自己建一個檔案試試看
# os.remove("./index.html")
#這個remove是強制執行，到資源回收桶也救不回來。
# os.rmdir("./newFolder")
print(list(os.walk("./many")))
#可以go through整個資料夾
#[('./many', [], ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt'])]
#------------------------------------------------------------------
folder_path = "./many"
shutil.rmtree(folder_path)
#完全刪除全部就算有檔案的folder