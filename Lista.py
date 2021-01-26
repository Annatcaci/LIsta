with open('input.txt','r') as f:
    a=list(eval(f.readline()))
print(a)
x=sorted(a)
print(a)
x.sort(reverse=True)
print(a)
print(len(a))
print(max(a))
print(min(a))
print(a+[111])
a[2]=222
print(a)
with open('output.txt','w') as f:
    f.write(str(x)+"\a")
   