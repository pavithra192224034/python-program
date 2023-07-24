lower = int(input("enter a number : "))
upper = int(input("enter a number : "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   
       for i in range(2, num):
           if (num % i) == 0:
              print(num)
              break
