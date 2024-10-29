with open ("myFile.txt", mode ="r") as my_file:
    all_content = my_file.read()
    print(all_content)
#用with open 就不需要去寫file.close()
#mode = 
#r-->預設(讀)
#-----------------------
#w-->write複寫(砍掉重寫)，如果此文件不存在會自動生成 write
#a-->append在現成的文件後面新增內容，如果此文件不存在會自動生成
#x --> create 生成文件，但如果已存在會報錯。

with open ("myFile2.txt", encoding="utf-8", mode ="w") as my_file:
    my_file.write("Learning python is a fun.\nLearning JavaScript is a fun, too.\n")
#改成w會被蓋過去
#想打中文要加encoding=utf-8