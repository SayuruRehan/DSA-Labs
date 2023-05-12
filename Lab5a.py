#Python program to find largest of two numbers

a = float(input("Enter num1: "))
b = float(input("Enter num2: "))

if(a > b):
    print("num1 is greater than num2".format(a, b))
elif(b > a):
    print("num1 is lesser than num2".format(b, a))
else:
    print("Both num1 and num2 are equal")

