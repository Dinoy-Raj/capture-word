file = input("Enter The File Name To Process")
coc = open(file)

data=dict()

for lines in coc:
    words = lines.split()
    for word in words:
        data[word] = data.get(word,0)+1

highwrd = None
highval = None

for wrd,val in data.items():
    if(highval is None):
        highval=val
        highwrd=wrd
    elif(val>highval):
        highval = val
        highwrd = wrd



print(highwrd,highval,"Times")

