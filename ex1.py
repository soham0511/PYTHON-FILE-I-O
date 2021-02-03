f=open("poems.txt",'r')
data=f.read()
if "twinkle" in data:
    print("Twinkle is present")
else:
    print("Twinkle not present")
    f.close()