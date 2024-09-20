import math

print("Hi in my calculator :] jest zajebisty")

num1 = float(input("Type first number: "))
print(" 1 = + \n 2 = - \n 3 = * \n 4 = / \n 5 = to 2nd power \n 6 = square root")
op = int(input("Type 1-6 to choose your operator: "))

if op == 5:
     print(f"The result is: {pow(num1, 2)}")
elif op == 6:
     print(f"The result is: {math.sqrt(num1)}")
else:
     num2 = float(input("Type second number: 5"))
     if op == 1:
          print(f"The result is: {num1+num2}")
     elif op == 2:
          print(f"The result is: {num1-num2}")
     elif op == 3:
          print(f"The result is: {num1*num2}")
     elif op == 4:
          print(f"The result is: {num1/num2}")


