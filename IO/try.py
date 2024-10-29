file = open('./myFile.txt')
# print(file.read(5))#參數可以指定讀多少內容
# file.seek(0)  #將指針滑到最上面
# print(file.read())#file.read會return一個string
# file.seek(0)
# print(file.readlines()) #return 一個list ['hello, how are you today?\n', 'I am fine thank you.']
for line in file.readlines():
    print(line)
while True:
    line = file.readline()
    if not line:
        break
    else:
        print(line)
file.close()#記得最後一定要關掉，不然開一個=Ram會被吃一個，太多最後ram會爆掉