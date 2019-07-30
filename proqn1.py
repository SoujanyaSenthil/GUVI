a=int(input())
l=[]
for i in range(0,a):
  b=input()
  l.append(b)
m=[]
for i in zip(*l):
  if (i.count(i[0])==len(i)):
    m.append(i[0])
  else:
      break
print(''.join(m))
