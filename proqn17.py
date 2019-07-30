o,a=map(int,input().split())
m=list(map(int,input().split()))
b=0
for i in range(0,o):
  for j in range(1,o):
    if l[i]+l[j]==a and i!=j:
      b=1
      break
print("yes" if b else "no")
