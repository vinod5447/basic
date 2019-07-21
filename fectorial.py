# fectorial numbe-------1*2*3*4*5=120
                        #1*2*6*24*120

n=int(input("enter number:"))

a=1

for i in range(1,n+1):
    a=a*i
    i=i+1
    print(a)
