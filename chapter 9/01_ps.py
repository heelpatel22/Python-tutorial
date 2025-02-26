f = open("file.txt")
data = f.read()
if("Twinkle" in data):
    print("The word is present.")
else:
    print("The word is not present.")
f.close()