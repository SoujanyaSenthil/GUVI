s=int(input())
m=0
b=[]
for s in range(1,s+1):
  b.append(s)
for s in range(len(b)):
  for s in range(s+1,len(b)):
    m+=1
print(m)
