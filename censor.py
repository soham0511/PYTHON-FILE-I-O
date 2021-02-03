with open("gully.txt") as f:
    content=f.read()

content=content.replace("donkey","$#%%#$$%#")

with open("gully.txt","w") as f:
    f.write(content)

