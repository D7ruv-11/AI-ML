tup = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
tup1=[]
tup2=[]
for i in tup :
    if i%2==0:
        tup1.append(i)
    else:
        tup2.append(i)   

t3= tuple(tup1)
t4= tuple(tup2)
print("even===>",t3, "odd===>",t4)
print(type(t3))
       
      






