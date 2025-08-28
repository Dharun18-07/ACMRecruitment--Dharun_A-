# Word Frequency Counter
t = "This is ACM recruitment where ACM takes students of amrita in their club and this is a example text"
t=t.lower()
c=""
for x in t:
    if x.isalnum() or x.isspace():
        c+=x
    else:
        c+=" "
w=c.split()
d={}
for x in w:
    if x in d:
        d[x]+=1
    else:
        d[x]=1
for x in d:
    print(x,"-",d[x])

    
