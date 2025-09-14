num = int(input("Enter user input number of factorial:"))
sum = 1
for i in range(num):
    sum + = sum *i
    print("factorial of given number =", sum)