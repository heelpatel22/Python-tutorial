words = ["Donkey","bad","ganda"]

with open("new.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#"*len(word))
with open("new.txt","w") as f:
    f.write(content)