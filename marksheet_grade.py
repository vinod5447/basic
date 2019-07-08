# if , elif , else

a = float(input("enter marks of subject:"))

if(a>=80)and(a<=100):
    print("1st class")
elif(a>=60)and(a<=79):
        print("2nd class")
elif(a>=40)and(a<=59):
        print("3rd class")
elif(a>=35)and(a<=39):
        print("pass")
elif(a>=0)and(a<=34):
        print("Fail")
elif(a<=-1):
        print("INVALID")
elif(a>=101):
        print("INVALID")
else:
    ()
