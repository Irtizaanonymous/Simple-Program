a1 = int(input("Enter Any Number:"))
a2 = int(input("Enter Any Number:"))
a3 = int(input("Enter Any Number:"))
a4 = int(input("Enter Any Number:"))

if a1>a2 and a1>a3 and a1>a4:
    print(f"The Greatest Number is: {a1}")
elif(a2>a1 and a2>a3 and a2>a4):
    print(f"The Greatest Number is: {a2}")
elif( a3>a1 and a3>a2 and a3>a4):
    print(f"The Greatest Number is: {a3}")
elif(a4>a1 and a4>a2 and a4>a3):
    print(f"The Greatest Number is: {a4}")