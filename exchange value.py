#example1: exchange value without 3rd varible

a = 10
b = 20

a = a + b  #10+20=30
b = a - b  #30-20=10
a = a - b  #30-10=20

print("a:",a)
print("b:",b)



#example2: exchange value without 3rd varible user

a = int(input("enter vlaue a:"))
b = int(input("enter vlaue b:"))


a = a + b
b = a - b  
a = a - b

print("a:",a)
print("b:",b)


#example3: exchange value within 3rd varible

a = int(input("enter vlaue a:"))  #40
b = int(input("enter vlaue b:"))  #30
c = 0

c = b  #0  =  40
b = a  #40 =  30
a = c  #30 =  0

print("a:",a)
print("b:",b)
