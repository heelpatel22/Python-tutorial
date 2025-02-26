word = "Donkey"

with open("new.txt","r") as f:
    content = f.read()

contentNew = content.replace(word,"######")
with open("new.txt","w") as f:
    f.write(contentNew)