A = set()
B = set()
C =set()
D =set()

A = {6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

B = {2,4,6,8,10,12,14,16,18,20,22,24}

C = {1, 4, 8, 10, 12, 15, 18, 20}

D = {2,3,5,7,11,13,17,19,23,29,31,37,41,43}

print("B ⋂(C⨁D)")
print(B.union(C.symmetric_difference(D)))

print("(A⋂C) ⋃B")    
print((A.intersection(C)).union(B))

print("(B⋃D) − C")
print((B.union(D)).difference(C))


print("(A − B) ⨁ (A⋂D)")
print((A.difference(B)).symmetric_difference(A.union(B)) )





