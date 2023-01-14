liste = ["1","2","3","4","5"]

a = ""

for node in liste:
    a += node
print(a)

print(a[2:])

liste.remove(liste[2:])

print(liste)