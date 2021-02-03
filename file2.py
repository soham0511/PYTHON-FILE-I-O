f=open("sample.txt")#if mode not specified then default is r
data=f.readline()#first line
print(data)
data=f.readline()#second line   
print(data)
data=f.readlines()#print lines as a list
print(data)
f.close()