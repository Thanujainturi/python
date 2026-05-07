from tabulate import tabulate
t=["name","age","dep"]
d=[["ravi",20,"cse"],
   ["sindhz",20,"csm"]]
res=tabulate(d,headers=t,tablefmt="grid")
print(res)
