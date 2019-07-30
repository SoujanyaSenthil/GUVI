la,ma=input().split()
s10=abs(len(ma)-len(la))
for s7 in range(len(la)):
  if(len(ma)==1 and ma[s7] in la):
    break
  if (la[s7]!=ma[s7]):
    s10=s10+1
print(s10)
