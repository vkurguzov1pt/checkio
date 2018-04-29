'''
data = (["X.O", "XX.", "XOO"])

s1 = "x.o|xx.|xoo"
s2 = "xxx|oxo|0.0"

for row in data:
    print(row)

for i in range(len(data)):
    print(i)

for i in range(len(data)):
    for row in data:
        print(i,row[i])
'''
data = ["XXX", "XX.", "XOO"]

def easyBreezy(row):
    print(row[0])

#print(all([x == 'X' for x in data[0]]))

map(easyBreezy, data)


#print(list(filter(lambda x: x[0]=='X', data)))