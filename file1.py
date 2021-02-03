f=open("sample.txt")#if mode not specified then default is r
data=f.read()
#data=f.read(4)#read first 4 charecters of files
print(data)
f.close()