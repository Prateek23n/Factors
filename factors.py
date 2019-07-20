def nfact(num):
    c=0
    for i in range(1,num+1):
        if(num%i==0):
            c=c+1
    if(c==0):
        s="None"
        return s
    else:
        return c
  
def sfact(num):
    s=0
    c=0
    for i in range(1,num+1):
        if(num%i==0):
            s=s+i
            c=c+1
    if(c==0):
        return -1
    else:
        return s
def fact(num):
    l=[]
    c=0
    for i in range(1,num+1):
        if(num%i==0):
            c=c+1
            l.append(i)
    if(c==0):
        return -1
    else:
        return l
def efact(num):
    l=[]
    c=0
    for i in range(1,num+1):
        if(num%i==0 and i%2==0):
            c=c+1
            l.append(i)
    if(c==0):
        return -1
    else:
        return l
def ofact(num):
    l=[]
    c=0
    for i in range(1,num+1):
        if(num%i==0 and i%2!=0):
            c=c+1
            l.append(i)
    if(c==0):
        return -1
    else:
        return l
def pfact(num):
    l=[]
    c=0
    p=0
    for i in range(1,num+1):
        if(num%i==0):
            c=c+1
            for j in range(1,i+1):
                if(i%j==0):
                    p=p+1
            if(p==2):
                l.append(i)
        p=0
    if(c==0):
        return -1
    else:
        return l
def epfact(num):
    l=[]
    c=0
    p=0
    for i in range(1,num+1):
        if(num%i==0):
            c=c+1
            for j in range(1,i+1):
                if(i%j==0):
                    p=p+1
            if(p==2 and i%2==0):
                l.append(i)
        p=0
    if(c==0):
        return -1
    else:
        return l
def sum_efact(num):
    l=[]
    c=0
    for i in range(1,num+1):
        if(num%i==0 and i%2==0):
            c=c+1
            l.append(i)
    if(c==0):
        return -1
    else:
        return sum(l)
def sum_ofact(num):
    l=[]
    c=0
    for i in range(1,num+1):
        if(num%i==0 and i%2!=0):
            c=c+1
            l.append(i)
    if(c==0):
        return -1
    else:
        return sum(l)
def sum_pfact(num):
    l=[]
    c=0
    p=0
    for i in range(1,num+1):
        if(num%i==0):
            c=c+1
            for j in range(1,i+1):
                if(i%j==0):
                    p=p+1
            if(p==2):
                l.append(i)
        p=0
    if(c==0):
        return -1
    else:
        return sum(l)

    


