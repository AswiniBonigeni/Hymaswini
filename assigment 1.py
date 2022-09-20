# list
l=[10,20,30,40,50,60,70,80,90]
print(l)
print(l[0])
print(l[1:4:3])
print(l[-8:-5])
print(l[-9:-2])
print(l[-3])
print(l[:4])
print(l[3:])

#tuple
T=("Hymaswini")
print(T)
print(T[0:5:2])
print(T[-9:-3])
print(T[3])
print(T[-6])
print(T[-8])
print(T[5:9])
print(T[4:])
print(T[:-5])

#dictionary
d={'w':'white','r':'red','b':'blue'}
print(d)
print(d['w'])
print("d=",d)

#frozen set
x=frozenset([10,20,30,40])
print(x)
x.add([50,60])
print(x)  #Syntax error because it does not allows modification
x.remove(10)
print(x)