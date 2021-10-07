a=[]
n=int(input('dati dimensiuna matricei 2..10'))
if n>=2 and n<=10:
    for i in range(0,n):
        v=[]
        for j in range(0,n)    
            k=int(input('dati elementele='))
            v.append([k])
            a.append([v])
print(a)
d_p=[]
d_s=[]

for i in range(len(a)):
    for j in range(len(a[0])):
        if i==j:
            d_p.append(a[i][j])
        if(i+j)==(len(a)-1):
            d_s.append(a[i][j])
print(sum(d_p)) 
print(sum(d_s)) 

dd_p=[]
ds_p=[] 
for i in range(len(a)):
    for j in range(len(a[0])):
        if i<j:
            dd_p.append(a[i][j])
        if i>j:
            ds_p.append(a[i][j])  
print(sum(dd_p)) 
print(sum(ds_p)) 

ds_deasupra=[]
ds_desupt=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        if i+j<(len(a)-1):
            ds_deasupra.append(a[i][j])
        if i+j>(len(a)-1):
            ds_desupt .append(a[i][j]) 
print(sum(ds_deasupra)) 
print(sum(ds_desupt))             




