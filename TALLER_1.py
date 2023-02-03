a=set()
b=set()

canta=int(input("INGRESE LOS VALORES DEL PRIMER CONJUNTO "))

for x in range(1,canta+1):
    cantidada= float(input("VALOR: "))
    a.add(cantidada)

cantb=int(input("INGRESE LOS VALORES DEL SEGUNDO CONJUNTO "))

for i in range(1,cantb+1):
    cantidadb= float(input("VALOR: "))
    b.add(cantidadb)

print(a)
print(b)

operation=int(input("ESCOJA LA OPERACIÓN A REALIZAR"))
print("1.UNIÓN")
print("2.INTERSECCIÓN")
print("3.DIFERENCIA ")
print("4. DIFERENCIA SIMÉTRICA")

if operation==1:
    z=a.union(b)
    print("CARDINALIDAD:",len(z))
    print(z)

if operation==2:
    z=a.intersection(b)
    print("CARDINALIDAD:",len(z))
    print(z)

if operation==3:
    z=a.difference(b)
    print("CARDINALIDAD:",len(z))
    print(z)

if operation==4:
    z=a.symmetric_difference(b)
    print("CARDINALIDAD",len(z))
    print(z)
