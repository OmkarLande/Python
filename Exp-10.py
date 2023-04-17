import arth
import even_odd
n=int(input("Enter operation you want to perform \n1.Arithmetic 2.Even_Odd \n"))
if (n==1):
    x=int(input("Enter a number "))
    y=int(input("Enter a number "))
    arth.add(x,y)
    arth.sub(x,y)
    arth.mul(x,y)
    arth.div(x,y)
elif(n==2):
    x=int(input("Enter a number "))
    even_odd.even(x)
else:
    print("Enter a valid number ")


