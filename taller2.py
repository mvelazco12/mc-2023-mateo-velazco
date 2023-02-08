a=set()
b=set()
c=set()
d=set()

A = {6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

B = {2,4,6,8,10,12,14,16,18,20,22,24}

C = {1, 4, 8, 10, 12, 15, 18, 20}

D = {2,3,5,7,11,13,17,19,23,29,31,37,41,43}

print("B ⋂(C⨁D)")
print(b.union(c.symmetric_difference(d)))

print("(A⋂C) ⋃B")    
print(a.intersection(c.union(b)))    

print("(B⋃D) − C")
print(b.union(d.difference(c)))


print("(A − B) ⨁ (A⋂D)")
print((a.difference(b)).symmetric_difference(a.union(b)) )