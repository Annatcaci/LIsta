nume=[]
with open('input.txt','r') as f:
    x=f.readlines()
for i in x:
    nume.append(i) 
nume=sorted(nume)
with open('output.txt','w') as f:
    f.writelines(nume)

