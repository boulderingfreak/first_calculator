# 1 +
# 2 -
# 3 *
# 4 /


print("Hi in my calculator.")

num1 = float(input("Type first number:"))
print(" 1 = + \n 2 = - \n 3 = * \n 4 = /")
op = int(input("Type 1-4 to choose your operator: "))
num2 = float(input("Type second number :"))

if op == 1:
    print(f"The result is: {num1+num2}")
elif op == 2:
     print(f"The result is: {num1-num2}")
elif op == 3:
     print(f"The result is: {num1*num2}")
elif op == 4:
     print(f"The result is: {num1/num2}")


