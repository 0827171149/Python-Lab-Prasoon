a=input()
upp=[]
low=[]
num=[]
for i in a:
 if(i.isalpha())==True:
    if(i.islower())==True:
        low.append(i)
    else:
          upp.append(i)
 else:
       num.append(i)
       
nume=[]
numod=[]
st=[]  
low.sort()
upp.sort()
num.sort()
for i in range(len(num)):
    if i%2==0:
     numod.append(i)
    else:
     nume.append(i)

st=low+upp+nume+numod;
print(st)

for i in st:
 print(i,end="")


