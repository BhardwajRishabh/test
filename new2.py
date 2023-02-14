from itertools import permutations
s="HACK"
li=list(permutations(s,2))
for i in li:
    print("".join(i))