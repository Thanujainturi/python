l=[4,2,3,4,8,3,4]
d={}
for i in l:
  if i in d:
    d[i]=d[i]+1
  else:
    d[i]=1
print(d)
