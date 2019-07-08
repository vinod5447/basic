# how to find series number===== 2+4+8+16+32

num=int(input("enter number:"))
x=0
y=1
for i in range(0,num):
    y=y*2
    z=x+y
    print(z)
