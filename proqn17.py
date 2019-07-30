so,sa=map(int,input().split())
m=list(map(int,input().split()))
b=0
for i in range(0,so):
  for j in range(m,so):
    if l[i]+l[j]==sa and i!=j:
      b=1
      break
print("yes" if p else "no")
