from itertools import combinations
a1,b1=map(int,input().split())
c1=len(str(a1))
d=list(combinations(str(a1),c1-b1))
d=sorted(d)
print(*d[0],sep='')
