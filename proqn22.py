ab=int(input())
cd=list(map(int,input().split()))
cd.sort(reverse=True)
b=0
b1=0
ef=[]
for i in range(0,ab,2):
  b=b+cd[i]
for j in range(1,ab,2):
  b1=b1+cd[j]
ef.append([b,b1])
for i in ef:
  print(i[0] if i[0]>i[1] else i[1])
