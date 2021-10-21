# Simple calculator 
opr = input ("What operation are you choosesing ? ( + , - , * , /): ")
a = float( input("Type first number: ") )
b = float( input("Type second number: ") )

if opr == "+":
    c = a + b 
    print("Result: " + str(c))
elif opr == "-":
    c = a - b 
    print("Result: " + str(c))
elif opr == "*":
    c = a * b 
    print("Result: " + str(c))
elif opr == "/":
    c = a / b 
    print("Result: " + str(c))       
else:
    print( "You are choosesing incorrect operation !!! " )
