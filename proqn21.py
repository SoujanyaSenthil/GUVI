s=int(input())
m=list(map(int,input().split()))
l=int(len(m)/2)
if sum(m[:l])//len(m[:l])==sum(m[l:])//len(m[l:]):
  print('yes')
else:
  print('no')
