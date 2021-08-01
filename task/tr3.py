

def sum2(x,y):
    return x+y
b= sum2(5,8)
print(b)
    


kh=["khaled","mohammed","naguib"]
for count,value in enumerate(kh):
    print(count)
    print(value)
    if count==1:
        print("you in loop one")
v=[2,42,6,9,5]

def mult10(s):
    return s*10

b=map(mult10,v)
print(list(b))

famm=["khaled","mohammed","yousef","ahmed"]
degr=[60,55,52,53]
merg=zip(famm,degr)
print (list(merg))

def filt1(n):
    if n>7:
        return True
    else:
        return False
res=filter(filt1,v)
print(list(res))
    
