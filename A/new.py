ops = ["5","2","C","D","+"]
"""now condition if num come add it 
if c come remove last element 
if d come append last element 2*last element 
if + come add last two element and add it


algo create a 
"""
sum = 0
l = []
for i in range(len(ops)):
    if ops[i].isnumeric():
        l.append(int(ops[i]))
    elif ops[i]=="C":
        l.pop()
    elif ops[i]=="D":
        l.append(2*l[-1])
    else:
        l.append((l[-1]+l[-2]))
print(l)
